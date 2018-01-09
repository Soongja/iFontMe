font2img
```sh
python font2img.py --src_font=src.ttf
                   --dst_font=tgt.ttf
                   --sample_dir=image_directory
                   --shuffle=1
                   --unicode=unicode_list.txt
                   --label=font_label
```

package
```sh
python package.py --dir=image_directory
                  --save_dir=binary_directory
                  --split_ratio=0.1
```

experiment layout
```sh
experiment/
└── data
    ├── train.obj
    └── val.obj
```

train
```sh
python train.py --experiment_dir=experiment 
                --experiment_id=your_experiment_num
                --batch_size=16 
                --lr=0.001
                --epoch=20 
                --sample_steps=100 
                --schedule=10
                --checkpoint_steps=100
```

infer
```sh
python infer.py --model_dir=checkpoint_dir/
                --batch_size=16 
                --source_obj=binary_obj_path 
                --embedding_ids=font label[s] of the font, separate by comma
                --save_dir=save_dir/
```
