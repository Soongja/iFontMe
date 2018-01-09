## font labels
0 - NanumGothic (SOURCE)


1 - SecretDiary

2 - MyHandwritingM

3 - ThreeLeafClover

4 - Mother'sLetterM

5 - Hangseo

6 - LipM


99 - LoveStory (TARGET)

## usage
font2img
```sh
python font2img.py --src_font=src.ttf
                   --dst_font=tgt.ttf
                   --sample_dir=image directory
                   --shuffle=1
                   --unicode=unicode_list.txt
                   --label=font label
```

package
```sh
python package.py --dir=image directory
                  --save_dir=binary directory
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
                --experiment_id=your experiment number
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
                --source_obj=binary.obj 
                --embedding_ids=font label[s] of the font, separate by comma
                --save_dir=save_dir/
```
