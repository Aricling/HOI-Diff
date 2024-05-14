import os
import shutil


if __name__=="__main__":
    raw_behave_path="/data1/guoling/HOI-Diff/dataset/raw_behave"
    texts_path="/data1/guoling/HOI-Diff/dataset/texts"

    behave_data_list=[os.path.splitext(behave_data_name)[0] for behave_data_name in sorted(os.listdir(raw_behave_path))]
    texts_list=[os.path.splitext(text_name)[0] for text_name in sorted(os.listdir(texts_path))]

    # print(len(behave_data_list))
    # print(len(texts_list))

    print("in dataset but not in texts_list:")
    for behave_data_name in behave_data_list:
        if behave_data_name not in texts_list:
            print(behave_data_name)
            # shutil.rmtree(os.path.join(raw_behave_path, behave_data_name))

        # 检查一下空文件夹
        path=os.path.join(raw_behave_path, behave_data_name)
        contents=os.listdir(path)
        if len(contents)==0:
            print(behave_data_name)
            # shutil.rmtree(os.path.join(raw_behave_path, behave_data_name))
    
    print('***************************')

    print("in texts_list but not in dataset:")
    for text_name in texts_list:
        if text_name not in behave_data_list:
            print(text_name)
            # os.remove(os.path.join(texts_path, text_name+".txt"))