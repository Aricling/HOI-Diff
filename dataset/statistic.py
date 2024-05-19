import os
import shutil
import pandas as pd
import matplotlib.pyplot as plt


if __name__=="__main__":
    # raw_behave_path="/data1/guoling/HOI-Diff/dataset/raw_behave"
    # texts_path="/data1/guoling/HOI-Diff/dataset/texts"

    # behave_data_list=[os.path.splitext(behave_data_name)[0] for behave_data_name in sorted(os.listdir(raw_behave_path))]
    # texts_list=[os.path.splitext(text_name)[0] for text_name in sorted(os.listdir(texts_path))]

    # # print(len(behave_data_list))
    # # print(len(texts_list))

    # print("in dataset but not in texts_list:")
    # for behave_data_name in behave_data_list:
    #     if behave_data_name not in texts_list:
    #         print(behave_data_name)
    #         # shutil.rmtree(os.path.join(raw_behave_path, behave_data_name))

    #     # 检查一下空文件夹
    #     path=os.path.join(raw_behave_path, behave_data_name)
    #     contents=os.listdir(path)
    #     if len(contents)==0:
    #         print(behave_data_name)
    #         # shutil.rmtree(os.path.join(raw_behave_path, behave_data_name))
    
    # print('***************************')

    # print("in texts_list but not in dataset:")
    # for text_name in texts_list:
    #     if text_name not in behave_data_list:
    #         print(text_name)
    #         # os.remove(os.path.join(texts_path, text_name+".txt"))


    # # 统计各片段的时长并画图
    # period_len_list=[]
    # dataset_path="/data1/guoling/HOI-Diff/dataset/raw_behave"
    # all_dir_paths=[os.path.join(dataset_path, dir_name) for dir_name in os.listdir(dataset_path)]
    # for dir_path in all_dir_paths:
    #     clips=os.listdir(os.path.join(dir_path, 'clips_preprocessed'))
    #     for clip in clips:
    #         period_len=int(os.path.splitext(clip)[0].split('_')[2])-int(os.path.splitext(clip)[0].split('_')[1])+1
    #         period_len_list.append(period_len)

    # # data_series = pd.Series(period_len_list)
    # plt.hist(period_len_list, bins=None, alpha=0.7, color='blue', edgecolor='black')
    # plt.title(f'HOI-diff processed data distribution:total {len(period_len_list)}')
    # plt.xlabel("frames")
    # plt.ylabel("freq")
    # plt.savefig("/data1/guoling/HOI-Diff/static.png")

    dataset_path="/data1/guoling/HOI-Diff/dataset/raw_behave"
    dataset_name_list=os.listdir(dataset_path)

    test_list=[]
    with open("/data1/guoling/HOI-Diff/dataset/test.txt", "r") as f:
        for line in f:
            test_list.append(line.strip())
    # print("test_list:", test_list)

    train_list=[]
    with open("/data1/guoling/HOI-Diff/dataset/train.txt", "r") as f:
        for line in f:
            train_list.append(line.strip())
    # print("train_list:", train_list)

    in_dataset_but_not_in_txt_list=[]
    add_to_test_list=[]
    add_to_train_list=[]
    for clip_name in dataset_name_list:
        if (clip_name not in test_list) and (clip_name not in train_list):
            in_dataset_but_not_in_txt_list.append(clip_name)
            if "Date03" in clip_name:
                add_to_test_list.append(clip_name)
            else:
                add_to_train_list.append(clip_name)
    print("in_dataset_but_not_in_txt_list:", '\n', in_dataset_but_not_in_txt_list)
    print("add_to_test_list:", '\n', add_to_test_list)
    test_list.extend(add_to_test_list)
    print("add_to_train_list:", '\n', add_to_train_list)
    train_list.append(add_to_train_list)
    


