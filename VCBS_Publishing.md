# VCB-Studio 发布流程及操作参考

VCB-Studio 工作流程如下：

| 位置 | 脚本 | 压制 | 整理 | 复查 | 1st | 截图 | last |
| :--: | :--: | :--: | :--: | :--: | :-: | :--: | :--: |
| 总监 |  X   |      |      |  X   |  X  |  X   |      |
| 压制 |      |  X   |      |      |     |      |      |
| 整理 |      |      |  X   |      |     |      |      |
| 复查 |      |      |      |  X   |  X  |      |      |
| 发布 |      |      |      |      |  X  |      |  X   |

本文为表中发布所参与的步骤提供参考。下文中的格式与表达仅作为参考，根据每个发布任务的情况可以做适当的增减和更改，以让观众能够准确且容易地理解内容信息。

## 1st Call

在项目完成制作阶段后，需要分发成品至分流组并做显式通知。这个步骤称为 1st Call。具体操作上，总监或整理组会提供种子和度盘成品给发布组，然后由总监、整理组或发布员任意一人首先将种子发布至内部 PT 站 rzi.xeonse.com，再在分流组以 @全体成员 的方式通知 1st Call。通知中需要注明 R21 的种子下载链接以及度盘链接。目前一共有 A、B、C 三个分流组，原则上按顺序分配任务，除非遇到项目文件容量严重不平衡或其他特殊的情况。任何时候如果出现需要换种的情况应立即在分流组以 @全体成员 的方式通知暂停下载或做种。

1st Call 之后的各个环节都是发布员独自全权负责了，包括 **对外发布前的准备工作**、**last call / 公网发布** 以及 **主站更新**。发布员可以再对种子和成品文件做简单检查，然后根据个人时间和最近分流组的负载情况来安排 Last call 的时间。

## 1st Call = VCB-S 内部 PT 站点 r21.3333.moe 发布

在将任务上传至 r21 之前，发布员应在本地或盒子里存放一份完整的成品。发布需要使用发布员自己的 r21 账号登陆并打开<https://rzi.xeonse.com/upload.php>，然后开始填写页面：

|       条目 | 内容                                         |
| ---------: | :------------------------------------------- |
| `种子文件` | 点击 `选择文件` 上传种子文件                 |
|   `英文名` | 英文名默认使用种子文件名，一般情况下无需更改 |
|   `中文名` | 如实填写                                     |
|   `附标题` | 填写百度网盘地址                             |
|  `NFO文件` | 不管                                         |
|     `简介` | 如下                                         |

如果是新项目，**`描述`** 部分使用这个模板：

```BBCode
[quote]
这里填写整理组提供的来源列表。如需要，请将格式简化为形如
BD: XXXX@XXXX
Scan: {XXXX, XXXX, XXXX}@XXXX
CD: XXXX@XXXX(xxxx.com, xxxx.com) <!-- 注意放流者链接已由中括号改为小括号，因为 acg.rip 处理超链接时无法识别两个连续的中括号 -->
[/quote]

[code]
这里粘贴使用 mediainfo 得到的主要成品文件的媒体信息，一般是随意选择一集正片。
将其中的文件路径改成形如 "D:\SAYA IS ∞ LOLICON!\[VCB-Studio]..."
[/code]
```

根据论坛方面的建议，所有 TSDM 的资源都需要将域名改为 `tsdm39.com`，例如将 `https://www.tsdm39.net/forum.php` 改为 `https://www.tsdm39.com/forum.php`。请在发布前留意检查。

接下来在 `类型` 里给该任务分配分流组，`质量` 一栏为选填内容，可以忽略，`内容` 选择 `公网[允许公网tracker]`，然后勾选 `匿名发布`。检查无误后点击 `发布`。

成功发布后在分流组以 @全体成员 的方式通知任务，同时使用自动下载的种子进行一段时间的初始做种。当有其他分流组员下载完成并开始做种时便可停止。

---

## 对外发布前的准备工作

发布员需要在 last call 前收集到下列内容：

1. 从 <https://rzi.xeonse.com/torrents.php> 上对应的种子页面点击 `下载种子[原始文件]` 取得公网种子，请注意检查公网种子名没有 [R21] 标识，并且不含 r21 密钥。
2. 主要成品的 mediainfo \
   a. 如果是单纯的新片或重发，随意选择一集正片 \
   b. 如果是新片打包旧片的合集，选择新片部分的随意一集正片 \
   c. 如果重发的成品文件有改动，选择改动过的一集正片

3. 如果是新番，应该有总监提供的吐槽和截图，并翻译为英文版
4. 如果是重发，应该有整理组提供的修正说明，并翻译为英文版
5. 一份横向长度 800px 的 WebP 格式海报图，并已经上传至图床 <http://img.2222.moe/vcbs>
6. 一份横向长度 1400px 且横纵比 2:1 左右的 WebP 格式海报图

#### 画质吐槽和截图

画质吐槽是总监对原盘画质的评价和制作处理的总结。其中可能出现多处中英文混排，需要由发布员手动于每处中英文之间添加一个半角空格。具体规则请参阅 <https://www.zhihu.com/question/19587406/answer/12298128>。各公网站点的发布时还需要英文版的画质吐槽，如果技术总监没有提供，需要由发布员翻译成英文。翻译时不理解和不确定的地方可以在群里提问。截图是用来进行对比原盘和成品的成组图片，也由总监提供。

一般情况下，画质吐槽和内容标记之外的一些特殊词组里的中英文和数字之间不需要空格，包含且不限于：队员的马甲、番剧名称等。

#### 海报图的详细说明

海报图片可以使用动画的官方宣传海报图片，如果你对这部作品有爱的话也可以夹带私货，自选一张喜欢的图片，不过要注意尺度，不要使用 NSFW 的图片。例如，可以在待发布动画的 anidb.net 页面上找到官方海报图片，通过 Google 图片搜索找到分辨率更高的相同图片。无论采用哪种图片，有效分辨率不能过小（如果图片分辨率过低，可以尝试用 waifu2x 放大）。确认图片目视足够清晰，且没有明显压缩导致的画质劣化和严重偏色。图片可以适当裁剪以保证横纵比例合适，并缩放为横向 800 px，保存为质量 90 的 WebP 格式。

---

## Last Call = 公网发布

公网发布一般安排于 1st call 至少十二小时之后，但同样根据实际情况可以特殊安排。目前可以通过 r21 来观测当前组内做种人数来判断是否已经可以发布公网，一般来说在发布公网时对应分流组应有至少 90% 的组员做种。发布任务不忙的时候尽量间隔一个自然日左右的时间。公网发布时间一般为北京时间 12:00 至 18:00 之间。

公网发布之前请前往 Trello 将自己添加进对应的项目卡片，将状态改为 `发布中` 并且在发布栏署名。

公网发布环节需要手动发布两个站点，包括 BANGUMI.MOE（推送 SHARE.DMHY.ORG / ACG.RIP / ACGNX.SE / SHARE.ACGNX.SE）和 NYAA.SI。

### 发布 BANGUMI.MOE（推送 SHARE.DMHY.ORG / ACG.RIP / ACGNX.SE / SHARE.ACGNX.SE）

打开 <https://bangumi.moe> ，以发布组账号登陆，右侧点击 **`发布`**，选择 **`旧版本`**，开始写发布文。

首先填写 **`标题`**：

|    `标题` | 格式： `[组名] 中文 / ENGLISH / 日本語 位深 分辨率 编码 类型 [标注]`                                                                                                                                                                                                                                                                                                           |
| --------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|    `组名` | 与种子保持一致，但合作组名用**中文**                                                                                                                                                                                                                                                                                                                                           |
|    `中文` | 大体如同 U2，具体格式如下                                                                                                                                                                                                                                                                                                                                                      |
| `ENGLISH` | 大体如同 U2，具体格式如下                                                                                                                                                                                                                                                                                                                                                      |
|  `日本語` | 大体如同 U2，具体格式如下，如果英文和日文太长可以不要日文                                                                                                                                                                                                                                                                                                                      |
|    `位深` | `10-bit`, `8-bit` ...                                                                                                                                                                                                                                                                                                                                                          |
|  `分辨率` | `1080p`, `720p` ...                                                                                                                                                                                                                                                                                                                                                            |
|    `编码` | `HEVC`, `AVC`, `AVC/HEVC` ...                                                                                                                                                                                                                                                                                                                                                  |
|    `类型` | `BDRip`, `DVDRip` ...                                                                                                                                                                                                                                                                                                                                                          |
|    `标注` | `Fin` 普通完整季度的高画质版本 <br> `MP4 Ver` MP4 移动版本 <br> `S1-S3 + OVA Fin` 如果需要注明多季度合集**只**标注在这里 <br> `S1-S2 Reseed Fin` 重发同理 <br> 发布时根据情况灵活使用标注，如 `MOVIE Fin` `OVA Fin` `Kamigami Ver` `先行版` <br>标注内嵌字幕信息时使用全大写的 `CHS` `CHT`，双语字幕 `CHS&JPN` <br>标题中有多种标注时用 `+` 隔开，类似`S1-S3 + SP + MOVIE Fin` |

在填写非单季番的 `番名` 时，如果：

1. 是特殊类型的番名，比如 点兔、迷糊餐厅、食戟之灵 这样标题有变化的就照原标题，如果标题不明显也可以在末尾加标季度 tag；
2. 番名自带季度，类似 约战 Ⅲ、魔禁 Ⅲ、超炮 T 这样的，也照用原标题，末尾不再加标季度 tag；
3. 番名无变化，在番名之后空格，然后使用 `第三季` / `S3` / `Season 3` 等方式标注季度，末尾不再加标季度 tag；
4. 是多季度合集，使用第一季的番名，末尾加标季度 tag。

由于 BANGUMI.MOE 对标题长度的限制，一些超长番名的项目需要使用简写标题。目前的解决方法是在 BANGUMI.MOE 填写简称，在成功同步之后再手动登陆各个站点将标题改回正常标题。

**`标签`** 会在填写标题时自动生成，注意检查有没有包含不正确的标签，尤其是复制修改标题的时候。

然后选择 **`类别`**：

| **`类别`** | 适用情况                   |
| ---------: | :------------------------- |
|     `合集` | 适用于一般季番或多季度合集 |
|   `剧场版` | 适用于剧场版               |
|     `动画` | 适用于 OVA 或其它短篇      |
|     `其它` | 适用于演唱会等三次元作品   |

现在开始填写正文，无论什么情况都会有接下来这个 **`主体段`**。点击 `<>`，将下面框内的代码复制进去，然后进行编辑和增减。

注 1：`<!-->` 内的文字为解释说明，不会出现在正文中
注 2：如果本月有开坑计划，招人计划等，请在海报图后、正文前添加，格式可以参考以前的发布
注 3: 请保留教程中每一部分的 `<p></p>` 标签。这些标签起到分隔不同内容板块的作用
注 4: 无论何时，复制粘贴时请注意换行的问题（尤其是截图之间的空行）
注 5: 不要在可视化界面下编辑，可能会产生各种意料之外的问题。如果不小心做了修改，请在代码或纯文本编辑界面下清空内容重新复制模板代码

```html
<p>
    <!-- 整个主体段都在一个 <p></p> 内，段中没有 <hr>，断行请用 <br> = Ctrl/Shift + Enter -->
    <!-- 海报图 800px WebP 格式 -->
    <img src="http://img.2222.moe/images/2018/08/05/JustBecause_800px.webp" alt="JustBecause_800px.webp" /><br />
    <br /><!-- 空行 --><!-- 空行的原因是 ACG.RIP 进行 HTML->BBCode 时没有处理好 <p></p> -->

    <!-- 片名和编码 -->
    <!-- 三语名称 [+ 季度] + 内容性质 -->
    <!-- 例 1 -->中文 / ENGLISH / 日本語 BDRip <br />
    <!-- 例 2 -->中文 / ENGLISH / 日本語 S1-3 BDRip MP4 Ver <br />
    <!-- 例 3 -->中文 / ENGLISH / 日本語 BDRip MP4 Ver <br />
    <!-- 例 4 -->中文 / ENGLISH / 日本語 S1 + S2 + OVA BDRip Reseed <br />
    <!-- 如果名字太长，分别成行 -->
    中文 S2 BDRip <br />
    ENGLISH S2 BDRip <br />
    日本語 S2 BDRip <br />
    <br />
    <!-- 如果有内封或内嵌字幕，应该指出 -->
    内封原盘 ENG + JPN 字幕。<br />
    Embedded official ENG + JPN PGS.<br />
    <!-- 如果有内封、内嵌或外挂音轨，应该指出 -->
    部分剧集内封评论音轨。内封评论音轨。外挂 FLAC 5.1 + Headphone X。<br />
    Certain episodes contain commentary tracks. Embedded commentary track. MKA contains FLAC 5.1 + Headphone X.<br />
    <!-- 注意区分使用 内封 和 内嵌。内封指挂载在视频文件内的信息内容，可以提取出来；内嵌则一般不可提取。多数情况下 MKV 内的字幕和音轨都为内封，MP4 内为内嵌 -->
    <br /><!-- 空行 -->

    <!-- 首先感谢合作字幕组（如有）-->
    这个项目与 <strong>中文组名</strong> 合作，感谢他们精心制作的字幕。<br />
    <!-- 英文紧跟中文，不空行 -->
    This project is in cooperation with <strong>English Group Name</strong>. Thanks to them for elaborating Chinese subtitles.<br />
    <br /><!-- 空行 -->

    <!-- 总监吐槽，只带在高画质版本 -->
    画质 XXXXXX...<br /><!-- 确保行间是 <br> -->
    处理上 XXXXXX...<br />
    <!-- 英文紧跟中文不空行，但是如果中英文都是多段式的可以根据情况进行调整 -->
    This BD ...........<br /><!-- 确保行间是 <br> -->
    PP: XXXX, XXXX, ...<br />
    <br /><!-- 空行 -->
</p>
<hr /><!-- 横线 -->
```

如果是 **`新番`**，接下来带这一段：

```html
<p>
    <!-- 首先是来源感谢，小体积版不带，不再写出自 NYAA 的资源 -->
    感谢所有资源提供者 / Thanks to all resource providers: <br />
    BD: XXXX@XXXX... <br />
    SCAN: XXXX@XXXX... <br />
    CD: XXXX@XXXX... <br />
    <br /><!-- 空行 -->
</p>
<hr />
<p>
    <!-- 如果项目标题或文件名过长，请带下面两行提示，一般情况下不需要带 -->
    本项目文件名较长，下载时请注意存放路径，以免发生无法下载的情况。<br /><!-- 英文紧跟中文不空行 -->
    Please be mindful of long paths in this torrent to avoid download error. <br />
    <br /><!-- 空行 -->

    VCB-Studio 已不再保证收集作品相关 CD 和扫图资源，详情请参见 <a href="https://vcb-s.com/archives/14331">https://vcb-s.com/archives/14331</a>。<br />
    Please refer to <a href="https://vcb-s.com/archives/14331">https://vcb-s.com/archives/14331</a> for more information about that VCB-Studio will no longer guarantee to include relevant CDs and scans.<br />
    <br /><!-- 空行 -->
    有关 TSDM 合购区的详情请参见 <a href="https://www.tsdm39.com/forum.php?mod=viewthread&amp;tid=879923">https://www.tsdm39.com/forum.php?mod=viewthread&amp;tid=879923</a>。<br />
    Please refer to <a href="https://www.tsdm39.com/forum.php?mod=viewthread&amp;tid=879923">https://www.tsdm39.com/forum.php?mod=viewthread&amp;tid=879923</a> for more information about jointly purchased music.<br />
    <br /><!-- 空行 -->

    <!-- 然后跟教程 -->
    播放器教程索引： <a href="https://vcb-s.com/archives/16639" target="_blank">VCB-Studio 播放器推荐</a><br />
    中文字幕分享区： <a href="https://bbs.acgrip.com/" target="_blank">Anime 分享论坛</a><br />
    项目计划与列表： <a href="https://vcb-s.com/archives/138" target="_blank">VCB-Studio 项目列表</a><br />
    特殊格式与说明： <a href="https://vcb-s.com/archives/7949" target="_blank">WebP 扫图说明</a><br />
    <br /><!-- 空行 -->
</p>
<hr />
<p>
    <!-- 最后放截图，但是只带在高画质版本 -->
    Comparison (right click on the image and open it in a new tab to see the full-size one)<br />
    Source________________________________________________Encode <br />
    <!-- 这里两对图只是例子 -->
    <a href="http://img.2222.moe/images/2018/07/03/3768.png"><img src="http://img.2222.moe/images/2018/07/03/3768s.png" /></a> <a href="http://img.2222.moe/images/2018/07/03/3768v.png"><img src="http://img.2222.moe/images/2018/07/03/3768s.png" /></a><br />
    <br /><!-- 每组截图之间空行 -->
    <a href="http://img.2222.moe/images/2018/07/03/6647.png"><img src="http://img.2222.moe/images/2018/07/03/6647s.png" /></a> <a href="http://img.2222.moe/images/2018/07/03/6647v.png"><img src="http://img.2222.moe/images/2018/07/03/6647s.png" /></a><br />
    ...
</p>
```

如果是 **`重发`**，则接下来带这一段：

```html
<p>
    <!-- 先是修正说明 -->
    重发修正：<br />
    1. XXXXXXXXXX；<br />
    2. XXXXXXXXXXXX。<br />
    <br />
    Reseed comment:<br />
    1. XXXXXXXXXX; <br />
    2. XXXXXXXXXXXX. <br />
    <br /><!-- 空行 -->
</p>
<hr />
<p>
    <!-- 写法参照 U2 reseed，如果没有资源提供者则不带 -->
    感谢所有资源提供者 / Thanks to all resource providers: <br />
    BD: XXXX@XXXX... <br />
    SCAN: XXXX@XXXX... <br />
    CD: XXXX@XXXX... <br />
    <br /><!-- 空行 -->
</p>
<hr />
<p>
    <!-- 然后是重发计划说明 -->
    本次发布来自 VCB-Studio 旧作重发计划。我们会不定期重发过去发布过的合集，或为补充做种，或为修正制作错漏，或为整合系列合集。<br />
    <br /><!-- 空行 -->
</p>
<hr />
<p>
    <!-- 最后是教程 -->
    播放器教程索引： <a href="https://vcb-s.com/archives/16639" target="_blank">VCB-Studio 播放器推荐</a><br />
    中文字幕分享区： <a href="https://bbs.acgrip.com/" target="_blank">Anime 分享论坛</a><br />
    项目计划与列表： <a href="https://vcb-s.com/archives/138" target="_blank">VCB-Studio 项目列表</a><br />
    特殊格式与说明： <a href="https://vcb-s.com/archives/7949" target="_blank">WebP 扫图说明</a><br />
    <br /><!-- 空行 -->
</p>
```

填好发布文后再点击 `<>` 回到可视化界面检查一下渲染出来的样式正确，然后点击 **`Choose File`** 选择种子文件，发布身份选择 **`VCB-Studio`**，点上 **`团队同步`**，确认无误后点击 **`发布`** 完成工作。不要关页面，一会还要用。

### 发布 NYAA.SI

打开 <https://nyaa.si> 并使用团队账号登录，从顶栏点击 `Upload`，上传种子，标题与 BANGUMI.MOE 相同。

|                       `Category` | 说明                                     |
| -------------------------------: | :--------------------------------------- |
|     `Anime - English-translated` | 有官方英语 PGS 字幕                      |
| `Anime - Non-English-translated` | 没有官方英语 PGS 字幕，但有中文 ASS 字幕 |
|                    `Anime - Raw` | 其他情况                                 |

**`Infomation`** 填写 `https://vcb-s.com/archives/138`

**`Complete`** 当项目是完整季度时勾选

**`Remake`** <u>仅当</u> 该项目是从 nyaa 上的另一个版本派生时勾选，Reseed 重发项目不勾选。

**`Description`** 使用 html 至 markdown 转换器转换 BANGUMI.MOE 上的内容，在 `Preview`中检查格式是否正确（注意空行）。

### 公网发布收尾

完成 NYAA.SI 发布后，回到 BANGUMI.MOE 的发布页并来到底部查看推送链接，检查是否种子是否已经正常推送至 ACGNX.SE / ACG.RIP / SHARE.DMHY.ORG。 **如果推送失败，需要手动登陆对应站点进行补发。** 然后在分流组以 @全体成员 的形式通知已经公网发布 / Last Call。一般情况下，不需要删除在各个公网发布站点的旧发布贴。

正常的话至此得到各站点一共 6 个链接，形如：

```
https://bangumi.moe/torrent/xxxxxxxxxxxxx
https://www.acgnx.se/show-xxxxxxxxxxxxxxx.html
https://share.acgnx.se/show-xxxxxxxxxxxxxxx.html
https://acg.rip/t/xxxxx
https://share.dmhy.org/topics/view/xxx_xxxxxx.html
https://nyaa.si/view/xxxxxxx
```

### 需要编辑的情况

发布后若发现有错漏需要修改，请务必尽快登陆各个网站修改对应页面。

-   bangumi.moe: 页面标题右侧 `X` 的左侧有一个编辑按钮
-   share.acgnx.se: 页面顶部 `發佈資源` 是登陆入口。登陆完毕后在右侧 `管理自己發佈的資源` 或者 `聯盟發佈資源` 里找到发布的页面进行编辑
-   acgnx.se: 页面顶部 `Control Panel` 是登陆入口。登陆完毕后在右侧 `My Torrent List` 或者 `Union Resources` 里找到发布的页面进行编辑
-   acg.rip: 页面右上角绿色按钮登陆，之后点击蓝色头像，在弹出菜单选择 `VCB-Studio`，在列表中找到发布的页面进行编辑
-   share.dmhy.org: 页面右上角登入，从 `個人中心 > 管理聯盟發佈資源` 找到发布的页面进行编辑
-   nyaa.si: 页面右上角登陆，找到自己发布的页面后在标题左侧点击编辑按钮进行编辑

---

## 主站更新

新番一般是新建一个页面，重发一般是修改旧页面。如果 Reseed 打包了多个旧页面的内容，更新于其中最老的一个。实在不适合更新于旧页面的 Reseed，如伊藤计划系列的打包，也可以新建页面来发布。

在更新主站之前需要先回到 r21 相关项目的页面，复制 `人员名单` 里所有成员的名字，稍后写主站页面的时候会用到。

点击自己的账号，在页面左边栏 `文章 > 写文章` 打开新文章编辑页面。

首先填写 **`标题`**。需要注意的是，主站页面的标题体现该页下所有的番目和画质版本，这导致其与 BANGUMI.MOE 发布采用的规则并不完全一样。比如 `标注` 中不会出现 `MP4 Ver`，有多种位深时不写等。

|      标题 | 格式：`ENGLISH / 中文 位深 分辨率 编码 类型 [标注]`                         |
| --------: | :-------------------------------------------------------------------------- |
| `ENGLISH` | ...                                                                         |
|    `中文` | ...                                                                         |
|    `位深` | 10-bit, 如果有 8-bit 的版本则不写位深                                       |
|  `分辨率` | 1080p, 720p, 1080p/720p                                                     |
|    `编码` | HEVC, AVC, AVC/HEVC                                                         |
|    `类型` | BDRip, DVDRip                                                               |
|    `标注` | Fin, Reseed Fin, S1-S3 + OVA Fin, S1-S2 Reseed Fin，注意重发项目标记 Reseed |

然后填写 **`正文`**：

复制粘贴模板时需要删除 <!-- > 注释里的内容，不然会造成行间距过大的问题。

```html
<!-- 如果有合作字幕组，要有这段感谢（文字仅供参考） -->
这个项目与 <strong>中文组名</strong> 合作，感谢他们精心制作的字幕。

<!-- 放置画质吐槽 -->
这个番 XXXXXXXXXXXXXXXXXXXXXX...

<!-- 可选的发布吐槽 -->
好想看到会动的瑠衣酱 XXXXXXXXX ...

<!-- 如果有内封或内嵌字幕，应该指出 -->内封原盘 ENG + JPN 字幕。
<!-- 如果有内封、内嵌或外挂音轨，应该指出 -->内封评论音轨。外挂 FLAC 5.1 + Headphone X。

<!-- 可选的发布吐槽也可以在这里 -->
好想看到会动的瑠衣酱 XXXXXXXXX ...

<!-- 在这里放一个 `more` 标签用来指示 WordPress 做摘要分隔 -->
<!--more-->

<!-- 如果非常喜欢这部番的某首音乐，可以上传音乐并将播放器放在这里 -->
[audio]https://vcb-s.com/wp-content/uploads/xxxxxx[/audio] [hermit auto="1" loop="0" unexpand="0" fullheight="0"]remote#:4[/hermit]

<!-- 如果有大量的吐槽内容，比如对老婆的爱，可以将剩余的部分放在这里 -->
好想看到会动的瑠衣老婆 XXXXXXXXX ...

<!-- 如果是 Reseed 项目，在编辑器中选择 `info` box 添加说明 -->
[box style="info"] 重发修正：<!-- 放在 box 下第一行 -->
<!-- 然后空一行 -->
1. xxx 2. xxx [/box]

<!-- 然后是下载链接，在编辑器中选择 `download` box -->
[box style="download"] 10-bit 1080p HEVC (Reseed)
<!-- 在 box 下第一行紧跟着标注画质，位深，编码，如果是 Reseed 记得标 Reseed -->
<!-- 这里空行，然后下一行开始点击 `link` 粘贴刚才发布公网各站的链接，注意勾选 `在新标签页中打开链接` -->
<a href="https://bangumi.moe/torrent/xxxxxxxx" rel="noopener" target="_blank">https://bangumi.moe/torrent/xxxxxxxx</a>
<!-- 每个链接之间空行 -->
<a href="https://share.acgnx.se/show-xxxxxxxxxxxxxxx.html" rel="noopener" target="_blank">https://share.acgnx.se/show-xxxxxxxxxxxxxxx.html</a>
<!-- 每个链接之间空行 -->
<a href="https://www.acgnx.se/show-xxxxxxxx.html" rel="noopener" target="_blank">https://www.acgnx.se/show-xxxxxxxx.html</a>
<!-- 每个链接之间空行 -->
<a href="https://acg.rip/t/xxxxxx" rel="noopener" target="_blank">https://acg.rip/t/xxxxxx</a>
<!-- 每个链接之间空行 -->
<a href="https://share.dmhy.org/topics/view/xxxxxx.html" rel="noopener" target="_blank">https://share.dmhy.org/topics/view/xxxxxx.html</a>
<!-- 每个链接之间空行 -->
<a href="https://nyaa.si/view/xxxxxx" rel="noopener" target="_blank">https://nyaa.si/view/xxxxxx</a>
[/box]

<!-- 其它画质版本同理 -->
[box style="download"] 8-bit 720p HEVC

<a href="https://bangumi.moe/torrent/xxxxxxxx" rel="noopener" target="_blank">https://bangumi.moe/torrent/xxxxxxxx</a>

<a href="https://share.acgnx.se/show-xxxxxxxxxxxxxxx.html" rel="noopener" target="_blank">https://share.acgnx.se/show-xxxxxxxxxxxxxxx.html</a>

<a href="https://www.acgnx.se/show-xxxxxxxx.html" rel="noopener" target="_blank">https://www.acgnx.se/show-xxxxxxxx.html</a>

<a href="https://acg.rip/t/xxxxxx" rel="noopener" target="_blank">https://acg.rip/t/xxxxxx</a>

<a href="https://share.dmhy.org/topics/view/xxxxxx.html" rel="noopener" target="_blank">https://share.dmhy.org/topics/view/xxxxxx.html</a>

<a href="https://nyaa.si/view/xxxxxx" rel="noopener" target="_blank">https://nyaa.si/view/xxxxxx</a>
[/box]

<!-- 将旧页面更新为 Reseed 项目时，需要将之前的链接移至最底部并划掉 -->
<!-- 先丢一个横线分隔已经弃用的链接 -->
<hr />

<!-- 部分旧页面上有大量不知道该怎么处理的吐槽段，可以放在这里 -->
旧吐槽 [box style="download"] 10-bit 1080p AVC
<!-- 用 `del` 按钮划掉旧链接，如果遇到度盘链接或 720p 链接可以直接删除 -->
<del><a href="https://bangumi.moe/torrent/xxxxxxxx" rel="noopener" target="_blank">https://bangumi.moe/torrent/xxxxxxxx</a></del>

<del><a href="https://share.acgnx.se/show-xxxxxxxxxxxxxxx.html" rel="noopener" target="_blank">https://share.acgnx.se/show-xxxxxxxxxxxxxxx.html</a>

<del><a href="https://www.acgnx.se/show-xxxxxx.html" rel="noopener" target="_blank">https://www.acgnx.se/show-xxxxxx.html</a></del>

<del><a href="https://acg.rip/t/xxxxxx" rel="noopener" target="_blank">https://acg.rip/t/xxxxxx</a></del>

<del><a href="https://share.dmhy.org/topics/view/xxxx.html" rel="noopener" target="_blank">https://share.dmhy.org/topics/view/xxxx.html</a></del>

<del><a href="https://nyaa.si/view/xxxxxx" rel="noopener" target="_blank">https://nyaa.si/view/xxxxxx</a></del>
[/box]

<!-- 最后，如果题图采用了有名有姓的大触插画，在这里标注来源 -->
Image Credit: <a href="http://xxxxx" rel="noopener" target="_blank">who</a>

<!-- 考虑到部分观众的需求，现在每个项目的 MediaInfo 也以折叠的形式带在发布页的最下方。此处特地感谢 inori@网站组 提供的模板 -->
<label for="medie-info-switch" class="btn btn-inverse-primary" title="展开MediaInfo">MediaInfo</label>
<!-- 这里空一行 -->
<pre class="js-medie-info-detail medie-info-detail" style="display: none;">此处粘贴 R21 上提供的 MediaInfo</pre>
```

完成正文后来到页面右侧：\
**`发布时间`**：新番直接选择 **`立即发布`** 即可，使用旧页面重发的 Reseed 需要改为当前北京时间 \
**`分类目录`**：务必勾选 **`作品项目`**，然后根据分辨率如实选择，为演唱会项目额外选择 **`音乐/专题`** \
**`标签`**：不用管 \
**`特色图片`**：这个即是主站海报图，上传使用之前准备的 1400px 宽度海报图 \
回到右上方点击 **`预览`** 确认页面样式无误后，点击 **`发布`** 完成页面发布 / **`更新`** 完成页面更新。

Reseed 项目可能合并了主站上其它多个页面的内容。 \
如果存在这种情况，需要前往每个这样的页面，于其正文 `<!--more-->` 下方添加指向于 Reseed 页面的说明，但是不更新时间：

```html
[box style="info"]<!-- 然后在 box 下第一行**紧跟着**写 -->
本页面的作品已被更新的合集替代，请移步下载新版：
<!-- 这里空行，然后下一行开始点击 `link` 粘贴 Reseed 页面，注意勾选 `在新标签页中打开链接` -->
<a href="https://vcb-s.com/archives/xxxx" rel="noopener" target="_blank">https://vcb-s.com/archives/xxxx</a>
[/box]
```

然后前往 `作品项目列表` 页面，点击 `Google Sheet` 打开在线表格，进行如下两步操作：

1. 在 `Intended` 页面里，找到并删除（如果有）刚发布的项目
2. 在`Completed` 页面里，在最顶端的项目之上插入新的一行，并填写：

|                   项目 | 内容                                                                                                  |
| ---------------------: | :---------------------------------------------------------------------------------------------------- |
|                    UID | 格式为 **YY+MM+NO**，其中 NO 是当月**公网**发布的序号。Reseed 项目序号单独排列，并在 NO 前面加上 `RS` |
| Romanji Title / 项目名 | 照抄文章标题，使用 ALT+ENTER 在单元格内换行                                                           |
|                   Info | 项目性质，例如 `TV`, `TV(S1-3)`, `MOVIE`, Reseed 项目加标 `RS`                                        |
|                   Link | 文章页面的链接                                                                                        |

打开 Trello 项目管理页面，将刚发布项目的对应卡片的状态改为 `完工`，同时将 Google Sheet 上的序号加至卡片名称前， 例如 `[200101] XXX`，注意空格。然后将卡片归档。

至此整个发布流程完成。

---

附主要合作字幕组对应中英文名称。若有变动，请以总监 / 整理组提供的版本为准。

|       中文名称 | 英文名称         |
| -------------: | :--------------- |
|     千夏字幕组 | Airota           |
|     喵萌奶茶屋 | Nekomoe kissaten |
| 悠哈璃羽字幕社 | UHA-WINGS        |
|     诸神字幕组 | Kamigami         |
|     天香字幕社 | T.H.X            |
|   动漫国字幕组 | DMG              |
|     星空字幕组 | XKsub            |
|       茉语星梦 | MakariHoshiyume  |
|       风之圣殿 | FZSD             |
|     白恋字幕组 | Shirokoi         |
|       SweetSub | SweetSub         |
