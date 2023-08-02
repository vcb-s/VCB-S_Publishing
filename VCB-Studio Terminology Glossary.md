# VCB-Studio 术语对照表

本术语对照表为发布组翻译制作吐槽提供参考。

添加条目时请归入对应表格。如果需要添加额外备注，请使用脚注。

下列对应翻译均取自 [VCB-Studio 科普教程 6]( https://vcb-s.com/archives/4738 ) 或以往翻译惯例，特定场合下的翻译应与总监商讨。

如无特殊标记，英文词性均为名词。

------

| 一般词汇           | General                         |
| ------------------ | ------------------------------- |
| 原盘               | Source / BD source              |
| 画风               | Image style                     |
| 线条               | Lines / Lines and curves        |
| 平面               | Flat area<sup name="a1">[1](#f1)</sup>  |
| 纹理               | Texture                         |
| 暗场（图像的低亮度区域）| Dark area                       |
| 暗场（影片的低亮度场景）| Dark scene(s)                   |
| 交错                  | Interlaced                      |
| 码率                  | Bitrate                         |
| 参数                  | Parameter(s)                    |
| 还原度                | High quality (bitrate)<sup name="a2">[2](#f2)</sup>   / Visual similarity / Transparency     |
| 压制                  | Encoding                       |
| 原生分辨率             | Native resolution              |
| 轻微                  | (adj.) Mild / Slight / A bit   |
| 适当                  | (adj.) Some / Moderate         |
| 较强                  | (adj.) Significant / Strong    |
| 算法                  | Algorithm                      |
| 内封字幕              | Embedded subtitles             |
| 内嵌字幕              | Embedded hardcoded subtitles   | 
| 屏幕字字幕            | Forced subtitles               |
| 无障碍音轨            | Audio description              |

<b name="f1">1</b> 这里的平面指一幅图像中在空间上变化比较缓和的部分，如大块的填充色，与线条相对；
如果是视频格式里的所谓平面，则是 plane，例如亮度平面 luma plane，色度平面（有两个）chroma planes；

<b name="f2">2</b> 根据 LP 的解释，压制上的高还原度有约定俗成的表达方式 High quality 或者 High bitrate，其他语境再单独考虑。

------

| 瑕疵                | Artifacts                     |
| ------------------- | ----------------------------- |
| 色带                | Banding / Colour banding      |
| 锯齿                | Aliasing                      |
| 晕轮 / 振铃         | Haloing / Ringing             |
| 色块                | Blocking / Macroblocking      |
| 噪点                | Noise / Grain<sup name="a1">[2](#f2)</sup>|
| 彩色噪点 / 色度噪点 | Chroma noise / chroma grain    |
| 烂边 / 蚊噪         | DCT ringing  / DCT noise      |
| 拉丝 / 横纹         | Combing                       |
| 缟缟                | Stripes                       |
| 鬼影                | Blending / Ghosting           |
| 颜色越界            | (Chroma) Overflow / Underflow |
| 色度色带            | Chroma banding                |
| 色度锯齿            | Chroma aliasing               |
| 色度偏移            | Chroma shift                  |
| 色度溢出            | Chroma bleeding               |
| 重复场              | Duplicated fields             |
| 晃动                | Global motion / Pan           |
| 彩虹                | Rainbow                       |
| 点状斑纹            | Dot-crawl                     |
| 过度柔化            | Over blurring                 |

<b name="f2">2</b> 作为画风特点的噪点是 Grain，一般颗粒度较大；作为瑕疵的噪点是 Noise，不确定时可统一使用 Noise。

------

| 处理方法       | Pre-processing                                 |
| -------------- | ---------------------------------------------- |
| 去色带         | De-banding                                     |
| 抗锯齿         | Anti-aliasing                                  |
| 去晕轮         | De-ringing / De-haloing                        |
| 去色块         | De-blocking                                    |
| 降噪           | Denoising / Degrain                            |
| 反交错         | Deinterlacing                                  |
| 场匹配         | Field-matching                                 |
| 反交卷过带     | Inverse Telecine (IVTC)                        |
| 去缟缟         | De-combing                                     |
| 去鬼影         | De-blending / Ghost removal                    |
| 修复颜色越界   | Fix overflow / underflow                       |
| 处理色度锯齿   | Chroma anti-aliasing                           |
| 修复色度偏移   | (v.) Fix chroma shift                          |
| 修复色度溢出   | (v.) Fix chroma bleeding                       |
| 解决重复场     | (v.) Fix duplicated fields                     |
| 修复晃动       | De-pan                                         |
| 修复彩虹       | De-rainbow                                     |
| 去除点状斑纹   | Dot-crawl removal                              |
| 纹理强化       | Texture enhancing                              |
| 锐化           | Sharpening                                     |
| 自适应锐化     | Adaptive sharpening                            |
| 保护性锐化     | Protective sharpening                          |
| 补偿性锐化     | Contra-sharpening<br />Compensatory sharpening |
| 可控性锐化     | Controlled sharpening                          |
| 主动性锐化     | Active sharpening                              |
| 过度锐化       | Over sharpening                                |
| 缩放           | Scaling                                        |
| 拉伸 / 拉升（分辨率） | Upscaling                                |
| 可还原式拉升   | Revertible upscaling                           |
| 缩回（分辨率） | Descaling                                      |
| 还原 – 再重构 / 逆向拉伸重构  | Descaling and reconstruction     |
