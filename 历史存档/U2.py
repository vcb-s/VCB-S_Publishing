import pyperclip

# 工具函数
def clean(paste):
    '''
    takes an input string from pyperclip.paste()
    return a string that remove all the empty lines ('\r')
    '''
    line_list = paste.split('\r')
    paste_clean = ''.join(line_list)
    return paste_clean

def write_to_txt(text):
    TXT = open('U2.txt', 'w', encoding = 'utf-8')
    TXT.write(text)
    TXT.close()

# 需要生成的各个部分
def recruit():
    string = ''
    recruit = input('招新吗？有则输入任意字符然后回车，没有则直接回车：')
    if recruit:
        string += '\n'
        string += '[b]VCB-Studio 2019 秋季招新中。有兴趣的同学请访问我们的主站了解相关情况：https://vcb-s.com/archives/11199[/b]\n'
        string += '\n'
        print('# 警告：可能需要手动修改招新时间与链接')
    return string

def collaboration():
    string = ''
    string += '[quote=制作吐槽/Making_Comment]\n'

    sub_dict = {'千夏字幕组': 'Airota', '喵萌奶茶屋': 'Nekomoe kissaten',
                '悠哈璃羽字幕社': 'UHA-WINGS', '诸神字幕组': 'Kamigami',
                '天香字幕社': 'T.H.X', '动漫国字幕组': 'DMG',
                '星空字幕组': 'XKsub', '茉语星梦': 'MakariHoshiyume',
                '风之圣殿': 'FZSD', '白恋字幕组': 'Shirokoi',
                '西农YUI': 'YUI-7', '豌豆字幕组': 'BeanSub',
                'SweetSub': 'SweetSub'}
    print('现有字幕组名单:', sub_dict.keys())
    sub_ch1 = input('输入合作字幕组1中文名（无合作则直接按回车）：').strip()
    if sub_ch1:
        sub_en1 = sub_dict[sub_ch1]
        sub_ch2 = input('输入合作字幕组2中文名（没有则直接按回车）：').strip()
        if sub_ch2:
            sub_en2 = sub_dict[sub_ch2]
            string += f'感谢 [b]{sub_ch1}[/b] 和 [b]{sub_ch2}[/b] 精心制作的字幕。\n'
            string += f'Thanks to [b]{sub_en1}[/b] and [b]{sub_en2}[/b] for elaborating Chinese subtitles.\n'
            string += '\n'
        else:
            string += f'感谢 [b]{sub_ch1}[/b] 精心制作的字幕。\n'
            string += f'Thanks to [b]{sub_en1}[/b] for elaborating Chinese subtitles.\n'
            string += '\n'
    # 空行留给if else内添加
    return string

def comment():
    string = ''
    pyperclip.copy('')
    input('复制中文评论（注意中英文之间之间半角空格），然后回车')
    com_ch = clean(pyperclip.paste().strip())
    input('复制英文评论，然后回车')
    com_en = clean(pyperclip.paste().strip())
    pyperclip.copy('')
    input('复制其他评论，然后回车，没有则直接回车')
    com_other = clean(pyperclip.paste().strip())
    if com_other:
        string += f'{com_ch}\n{com_en}\n\n{com_other}\n'
    else:
        string += f'{com_ch}\n{com_en}\n'

    string += '[/quote]\n'
    string += '\n'
    return string

def staff():
    string = ''
    string += '[quote=感谢所有参与制作者/Thanks_to_our_participating_members]\n'

    staff_name = []
    staff_category = ['总监 / Script：', '压制 / Encode：', '整理 / Collate：',
                  '复查 / QC：', '发布 / Upload：', '分流 / Seed：']
    print('多人参与请手动用全角逗号“，”分开')
    for i in range(len(staff_category)-1):
        name = input('输入 ' + staff_category[i]).strip()
        staff_name.append(name)
    staff_name.append('VCB-Studio CDN 分流成员（详细名单见主站）')
    print('分流成员信息已自动生成')
    for j in range(len(staff_category)):
        string += staff_category[j] + staff_name[j] + '\n'

    string += '[/quote]\n'
    string += '\n'
    return string

def source():
    string = ''
    string += '[quote=感谢所有资源提供者/Thanks_to_all_resource_providers]\n'

    pyperclip.copy('')
    input('前往R21，复制资源提供者信息（包含链接），然后回车')
    paste = clean(pyperclip.paste().strip())
    string += f'{paste}\n'

    string += '[/quote]\n'
    string += '\n'
    return string

def mediainfo():
    string = ''
    string += '[spoiler=mediainfo][mediainfo]\n'

    pyperclip.copy('')
    input('前往R21，复制媒体信息，然后回车')
    paste = clean(pyperclip.paste().strip())
    string += f'{paste}\n'

    string += '[/mediainfo][/spoiler]\n'
    string += '\n'
    return string

def screenshot():
    string =''
    string += '[spoiler=screenshots]\n'

    print('# 警告：请提前检查图片链接是否有效')
    pyperclip.copy('')
    input('请到总监吐糟中，复制[IMG]开头结尾的代码（从Comparison开始），然后回车')
    paste = clean(pyperclip.paste().strip())
    string += f'{paste}\n'

    string += '[/spoiler]\n'
    string += '\n'

    return string

def comment_reseed():
    string = ''

    pyperclip.copy('')
    input('复制之前帖子上的中文评论（注意中英文之间之间半角空格），然后回车')
    com_ch = clean(pyperclip.paste().strip())
    input('复制之前帖子上的英文评论，然后回车')
    com_en = clean(pyperclip.paste().strip())

    string += f'{com_ch}\n{com_en}\n'

    string += '[/quote]\n'
    string += '\n'
    return string

def reseed_info():
    string = ''
    string += '[quote=重发修正/Reseedd_Info]\n'

    pyperclip.copy('')
    input('复制重发修正的的中文说明（注意中英文之间之间半角空格），然后回车')
    com_ch = clean(pyperclip.paste().strip())
    input('复制重发修正的的英文说明，然后回车')
    com_en = clean(pyperclip.paste().strip())

    string += f'{com_ch}\n{com_en}\n'

    string += '[/quote]\n'
    string += '\n'
    return string

def mediainfo_reseed():
    string =''
    string += '[spoiler=mediainfo][mediainfo]'

    pyperclip.copy('')
    input('复制重发视频的媒体信息，如果没有，从旧帖子里复制过来')
    paste = clean(pyperclip.paste().strip())
    string += f'{paste}\n'

    string += '[/mediainfo][/spoiler]\n'
    string += '\n'
    return string

# 新番/重发
def new_project():
    str_parts = []

    str_parts.append(recruit())
    str_parts.append(collaboration())
    str_parts.append(comment())
    str_parts.append(staff())
    str_parts.append(source())
    str_parts.append(mediainfo())
    str_parts.append(screenshot())
    text = ''.join(str_parts)
    return text

def reseed():
    str_parts = []

    str_parts.append(recruit())
    str_parts.append(collaboration())
    str_parts.append(comment_reseed())
    str_parts.append(reseed_info())
    str_parts.append(mediainfo_reseed())

    text = ''.join(str_parts)
    return text

# 主程序
print('#本工具将生成用于U2发布的代码txt')
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

