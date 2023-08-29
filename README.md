# YOLOv8 Auto Trainer

## Prerequisites

NixOS:

```bash
nix-shell
```

Other systems:

```bash
python3 -m venv venv # must have Python 3.9+ installed
source venv/bin/activate
pip install -r requirements-no-nix.txt
```

1. Record spinning videos of objects

2. 1-prepare-input

3. Download checkpoint

https://github.com/facebookresearch/segment-anything#model-checkpoints
vit-b

wget -O sam_vit_b_01ec64.pth https://dl.fbaipublicfiles.com/segment_anything/sam_vit_b_01ec64.pth

2. Copy them into `input` folder, then create masks by running:

   ```bash
   ./2-create-masks
   ```
