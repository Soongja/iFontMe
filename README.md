## font labels
0 - NanumGothic (SOURCE)

1 - SecretDiary

2 - MyHandwritingM

3 - ThreeLeafClover

4 - Mother'sLetterM

5 - Hangseo

6 - LipM

7 - BMHANNA11yrs

8 - BMJUA

9 - SeoulHangangM

10 - Gorae

11 - KindergartenM

12 - nambuk

99 - LoveStory (TARGET)

## usage
font2img
```sh
python font2img.py --src_font=src.ttf
                   --dst_font=tgt.ttf
                   --sample_dir=image save directory
                   --shuffle=1(otherwise, 0)
                   --unicode=unicode_list.txt
                   --label=font label(integer)
                   --sample_count=number of characters you want to create(integer)
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
