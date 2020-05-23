import os
import random
import shutil
import time

def check(current_dir):
    print(current_dir)
    if 'PM' not in current_dir:
        print('当前目录没有PM文件夹')
        os.mkdir('PM')
    if 'backup' not in current_dir:
        print('当前目录没有backup备份文件夹')
        os.mkdir('backup')

def work():
    files_list = []
    dirs_list = []
    work_dir_path = current_dir_path + '/PM'
    os.chdir(work_dir_path)
    file_list = os.listdir()
    print('正在查找文件')
    for file in file_list:
        if os.path.isfile(file):
            files_list.append(file)
        else:
            dirs_list.append(file)
    for x in files_list:
        for y in dirs_list:
            if x.split('.')[0] in y.split('+'):
                if os.path.exists(x):
                    xx = '{}/{}'.format(work_dir_path, x)
                    yy = '{}/{}/{}'.format(work_dir_path, y, x)
                    shutil.move(xx, yy)               
                print('正在移动[{}]到---------->[{}]文件夹中'.format(x, y))



def work2():
    files = []
    dirs = []
    work_dir_path = current_dir_path + '/PM'
    os.chdir(work_dir_path)
    print(os.getcwd())
    file_list = os.listdir()
    print('正在查找文件')
    for x, y, z in os.walk(work_dir_path):
        # print(x,z)
        if len(z) !=0:
            xx = x
            yy = '{}/{}'.format(work_dir_path, z[0])
            zz = '{}/{}'.format(x, z[0])
            print(yy, zz)
            shutil.move(zz, yy)

def gen():
    work_dir_path = current_dir_path + '/PM'
    os.chdir(work_dir_path)
    times=100
    i = 0
    while i < times:
        i += 1
        x = ['赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯', '陈', '褚', '卫', '蒋', '沈', '韩', '杨', '朱', '秦', '尤', '许', '何', '吕', '施', '张', '孔', '曹', '严', '华', '金', '魏', '陶', '姜', '戚', '谢', '邹', '喻', '柏', '水', '窦', '章', '云', '苏', '潘', '葛', '奚', '范', '彭', '郎', '鲁', '韦', '昌', '马', '苗', '凤', '花', '方', '俞', '任', '袁', '柳', '酆', '鲍', '史', '唐', '费', '廉', '岑', '薛', '雷']
        ming_male_list = ['伟', '勇', '军', '磊', '涛', '斌', '强', '鹏', '杰', '峰', '超', '波', '辉', '刚', '健', '明', '亮', '俊', '飞', '凯', '浩', '华', '平', '鑫', '毅', '林', '洋', '宇', '敏', '建', '兵', '旭', '雷', '锋', '彬', '龙', '翔', '阳', '剑', '东', '博', '威', '海', '巍', '晨', '炜', '帅', '岩', '江', '松', '文', '云', '力', '成', '琦', '进', '昊', '宏', '欣', '坤']
        ming_female_list = ['静','敏','燕','艳','丽','娟','莉','芳','萍','玲','娜','丹','洁','红','颖','琳','霞','婷','慧','莹','晶','华','倩','英','佳','梅','雪','蕾','琴','璐','云','蓉','青','薇','欣','琼','宁','平','媛','虹','杰','婧','雯','茜','楠','洋','君','辉','菲','琦','妍','瑜','蕊','宇','明','珊','琪','玉','怡','文','岚','婕','凤','芬','芸','晓','萌','露','菁','惠','蓓','璇']
        bianhao = random.randint(10000, 99999)
        xing = random.choice(x)
        ming_male_1 = random.choice(ming_male_list)
        ming_female_1 = random.choice(ming_male_list)
        ming_female_2 = ''.join(random.sample(ming_female_list, 2))
        ming_male_2 = ''.join(random.sample(ming_male_list, 2))
        ming = random.choice([ming_male_1, ming_female_2, ming_male_2, ming_female_1])
        
        dir_name = '00000{}+{}'.format(bianhao, xing+ming)
        file_name = '00000{}.xlsx'.format(bianhao)
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)
        if not os.path.exists(file_name):
            f = open(file_name, 'w')
            f.close()
        print('{}:正在生成文件夹[{}]和文件[{}]'.format(i, dir_name, file_name))



if __name__ == "__main__":
    t1= time.time()
    current_dir_path = os.getcwd()
    current_dir_list = os.listdir(current_dir_path)   
    check(current_dir_list)
    # work2()
    gen()
    time.sleep(10)
    work()
    t2 = time.time()
    print('{}耗时'.format(t2-t1))

