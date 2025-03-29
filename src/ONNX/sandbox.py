import torch
import torch.nn as nn
from pathlib import Path

src_dir = Path("src/ONNX")

class MLPModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc0 = nn.Linear(8, 8, bias=True)
        self.fc1 = nn.Linear(8, 4, bias=True)
        self.fc2 = nn.Linear(4, 2, bias=True)
        self.fc3 = nn.Linear(2, 2, bias=True)

    def forward(self, tensor_x: torch.Tensor):
        tensor_x = self.fc0(tensor_x)
        tensor_x = torch.sigmoid(tensor_x)
        tensor_x = self.fc1(tensor_x)
        tensor_x = torch.sigmoid(tensor_x)
        tensor_x = self.fc2(tensor_x)
        tensor_x = torch.sigmoid(tensor_x)
        output = self.fc3(tensor_x)
        return output


model = MLPModel()
tensor_x = torch.rand((97, 8), dtype=torch.float32)
dynamic_shapes = {
    "input": {0: "batch_size", 1: "sequence_length"}  # Dynamically define batch and sequence length
}

# onnx_program = torch.onnx.export(model, (tensor_x,), dynamo=True)
# onnx_program.save("src/ONNX/mlp.onnx")

tt = torch.onnx.export(
    model,  # model to export
    (tensor_x,),  # inputs of the model,
    src_dir / "my_model.onnx",  # filename of the ONNX model
    # input_names=["input"],  # Rename inputs for the ONNX model
    dynamo=True,  # True or False to select the exporter to use
    dynamic_shapes=dynamic_shapes
)

# export_options = torch.onnx.ExportOptions(dynamic_shapes=True)
# onnx_program = torch.onnx.dynamo_export(
#     model, (tensor_x,), export_options=export_options
# )
# onnx_program.save("my_dynamic_model.onnx")

import onnx

onnx_model = onnx.load(src_dir / "my_model.onnx")
for input in onnx_model.graph.input:
    print(input.name, input.type.tensor_type.shape.dim)