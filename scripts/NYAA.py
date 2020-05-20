import pyperclip
import re

# 工具函数
def write_to_txt(text):
    TXT = open('NYAA.txt', 'w', encoding = 'utf-8')
    TXT.write(text)
    TXT.close()

def clean(paste):
    line_list = paste.split('\r')
    paste_cleaned = ''.join(line_list)
    return paste_cleaned

def check_punctuation(text):
    punc_string = '，。；：‘“’”？！（）【】'
    for elem in text:
        if elem in punc_string:
            print(f'找到中文标点 {elem} ，请手动清除！')

# 需要生成的各个部分
def poster():
    string = ''

    poster_url = input('输入宽度800海报的链接，然后回车：').strip()
    string += f'![]({poster_url})\n'
    # poster_raw = input('有爱请输入原图链接，没有则直接回车：').strip()
    # if poster_raw:
    #    string += f'![![]({poster_raw})]({poster_url})\n'

    string += '\n'
    return string

def info(name_long):
    string = ''

    name_en = input('输入英文番名，然后回车：').strip()
    name_jp = input('输入日文番名，然后回车：').strip()
    print('# 作品性质范例：')
    print('# BDRip')
    print('# S1-3 BDRip')
    print('# BDRip MP4 Ver')
    print('# S1+S2+OVA BDRip Reseed')
    package_type = input('输入作品性质，然后回车：').strip()
    if name_long:
        string += f'{name_en} {package_type}\n'
        string += f'{name_jp} {package_type}\n'
    else:
        string += f'{name_en} / {name_jp} {package_type}\n'
    print('# 格式及大小范例：')
    print('# 10-bit 1080p HEVC + FLAC + AAC, MKV format. ~ 1.1 GB / EP.')
    print('# 8-bit 720p HEVC + AAC, MP4 format. ~ 250 MB / EP.')
    format_and_size = input('输入格式及大小，然后回车：').strip()
    string += f'{format_and_size}\n'

    subtitle = input('输入内嵌字幕信息，没有则直接回车：').strip()
    if subtitle:
        string += f'{subtitle}\n'
    track = input('输入内嵌/外挂音轨信息，没有则直接回车：').strip()
    if track:
        string += f'{track}\n'

    string += '\n'
    return string

def collaboration():
    string = ''

    sub_dict = {'千夏字幕组': 'Airota', '喵萌奶茶屋': 'Nekomoe kissaten',
                '悠哈璃羽字幕社': 'UHA-WINGS', '诸神字幕组': 'Kamigami',
                '天香字幕社': 'T.H.X', '动漫国字幕组': 'DMG',
                '星空字幕组': 'XKsub', '茉语星梦': 'MakariHoshiyume',
                '风之圣殿': 'FZSD', '白恋字幕组': 'Shirokoi',
                '西农YUI': 'YUI-7', '豌豆字幕组': 'BeanSub',
                'SweetSub': 'SweetSub'}
    print('现有字幕组名单:', sub_dict.keys())
    sub_ch1 = input('输入合作字幕组1中文名（无合作直接按回车）：').strip()
    if sub_ch1:
        sub_en1 = sub_dict[sub_ch1]
        sub_ch2 = input('输入合作字幕组2中文名（没有则直接按回车）：').strip()
        if sub_ch2:
            sub_en2 = sub_dict[sub_ch2]
            string += f'Thanks to **{sub_en1}** and **{sub_en2}** for elaborating Chinese subtitles.\n'
            string += '\n'
        else:
            string += f'Thanks to **{sub_en1}** for elaborating Chinese subtitles.\n'
            string += '\n'
    # 空一行的任务交给 if else 内了，和 BAMGUMI 一样
    return string

def comment(mobile_version):
    if mobile_version:
        return ''
    else:
        string = ''

        pyperclip.copy('')
        input('从bangumi.moe复制英文吐槽，然后回车')
        com_en = clean(pyperclip.paste().strip())
        string += f'{com_en}\n'

        string += '\n***\n\n'
        return string

def staff(mobile_version):
    if mobile_version:
        return ''
    else:
        string = ''

        string += 'Thanks to our participating members:'
        string += '\n'
        staff_name = []
        staff_category = ['Script: ', 'Encode: ', 'Collate: ',
                      'QC: ', 'Upload: ', 'Seed: ']
        print('请对照bangumi.moe制作人员列表，填写以下内容')
        for i in range(len(staff_category)-1):
            name = input('输入 ' + staff_category[i]).strip()
            staff_name.append(name)
        staff_name.append('Seeding members of VCB-Studio CDN (refer to our website for full list)')
        print('分流成员信息已自动生成')
        for j in range(len(staff_category)):
            string += staff_category[j] + staff_name[j] + '\n'

        string += '\n'
        return string

def source(mobile_version):
    if mobile_version:
        return ''
    else:
        string = ''

        pyperclip.copy('')
        input('对照bangumi.moe，复制来源信息，然后回车')
        paste = clean(pyperclip.paste().strip())
        string += f'Thanks to all resource providers:\n{paste}\n'

        string += '\n***\n\n'
        return string

def miscellaneous(name_long):
    string = ''

    if name_long:
        string += '**Please be mindful of long paths in this torrent to avoid download error.**\n'
        string += '\n'
    WebP = input('有WebP扫图吗？有输入任意字符然后回车，没有直接回车：')
    if WebP:
        string += 'Please refer to https://vcb-s.com/archives/7949 if you have trouble viewing WebP images.'
        string += '\n'

    string += '\n***\n\n'
    return string

def screenshot(mobile_version):
    SUFFIX = r'\.png\)'
    REPLACE_SUFFIX = '.png)'

    string = ''                                                                                                                        │

    if not mobile_version:                                                                                                                     │
        pyperclip.copy('')                                                                                                                 │
        input('请到总监吐糟中，复制[![](开头的代码（从Comparison开始），然后回车')                                                         │
        string = pyperclip.paste().strip()                                                                                                 │

        # check empty-line in between
        if (re.findall(SUFFIX + '\n\n', string, re.M) == []):                                                                              │
            string = re.sub(SUFFIX + '\n', REPLACE_SUFFIX + '\n\n', string, re.M)                                                          │

        if (re.findall(SUFFIX + '\r\n\r\n', string, re.M) == []):                                                                          │
            string = re.sub(SUFFIX + '\r\n', REPLACE_SUFFIX + '\r\n\r\n', string)                                                          │

    return string

def reseed_info():
    string = ''

    string += 'Reseed comment:\n'

    pyperclip.copy('')
    input('复制英文的重发修正，然后回车')
    com_en = pyperclip.paste().strip()
    string += f'{com_en}\n'

    string += '\n***\n\n'

    string += 'This is a release of VCB-Studio Monthly Reseed Project.\n'
    string += 'In the middle and the end of each month we shall renew previous torrents which may be:\n'
    string += '\n'
    string += '1. of zero or few seeders so reseeding is required to resurrect it;\n'
    string += '2. with some missing clips/mistakes so we would like to revise it;\n'
    string += '3. separated releases that can be batched into a single torrent.\n'
    print('# 重发时间范例：')
    print('# August 2019, middle')
    reseed_date = input('输入本次重发时间（注意空格）：').strip()
    string += (reseed_date)

    return string

# 新番/重发
def new_project():
    str_parts = []

    str_parts.append(poster())
    global long
    long_name = input('番名长吗？长则输入任意字符然后回车，没有则直接回车：')
    if long_name:
        long = True
    else:
        long = False
    str_parts.append(info(long))
    str_parts.append(collaboration())
    global mobile
    mobile = input('是小体积版吗？是则输入任意字符然后回车，没有直接回车：')
    str_parts.append(comment(mobile))
    str_parts.append(staff(mobile))
    str_parts.append(source(mobile))
    str_parts.append(miscellaneous(long))
    str_parts.append(screenshot(mobile))

    text = ''.join(str_parts)
    check_punctuation(text)
    return text

def reseed():
    str_parts = []

    str_parts.append(poster())
    global long
    long_name = input('番名长吗？长则输入任意字符然后回车，没有则直接回车：')
    if long_name:
        long = True
    else:
        long = False
    str_parts.append(info(long))
    str_parts.append(collaboration())
    # 目前是reseed不考虑小体积版
    str_parts.append(reseed_info())

    text = ''.join(str_parts)
    check_punctuation(text)
    return text

# 主程序
print('#本工具将生成 nyaa.si 发布代码')
print('#请注意区分“输入”和“复制”')
while True:
    project_type = input('新番（1）或重发项目（2）：')
    if project_type not in ['1', '2']:
        print('请输入数字"1"或"2"')
    else:
        if project_type == '1':
            output_text = new_project()

            break
        else:
            output_text = reseed()
            break
write_to_txt(output_text)
input('（按回车退出）')

