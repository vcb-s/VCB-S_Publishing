# VCB-Studio 术语对照表

本术语对照表为发布组翻译制作吐槽提供参考。

添加条目时请归入对应表格。如果需要添加额外备注，请使用脚注。

下列对应翻译均取自 [VCB-Studio 科普教程 6](https://vcb-s.com/archives/4738) 或以往翻译惯例，特定场合下的翻译应与总监商讨。

如无特殊标记，英文词性均为名词。

| 一般词汇                 | General                                                      |
| ------------------------ | ------------------------------------------------------------ |
| 原盘                     | source / Blu-ray source / BD source                          |
| 画风                     | art style                                                    |
| 线条                     | lines / lines and curves                                     |
| 平面（相对于线条 [^1]）  | flat area                                                    |
| 纹理                     | texture                                                      |
| 暗场（图像的低亮度区域） | dark area                                                    |
| 暗场（影片的低亮度场景） | dark scene(s)                                                |
| 交错                     | (adj.) interlaced                                            |
| 平面（图像格式 [^2]）    | plane                                                        |
| 亮度平面（图像格式）     | luma plane                                                   |
| 色度平面（图像格式）     | chroma plane(s)                                              |
| 码率                     | bitrate                                                      |
| 参数                     | parameter(s)                                                 |
| 清晰度                   | sharpness                                                    |
| 还原度                   | (high) quality/bitrate <br> visual similarity / transparency |
| 压制                     | encoding                                                     |
| 原生分辨率               | native resolution                                            |
| 轻微                     | (adj.) mild / slight / a bit                                 |
| 适当                     | (adj.) some / moderate                                       |
| 较强                     | (adj.) significant / strong                                  |
| 算法                     | algorithm                                                    |
| 内封字幕                 | embedded subtitles                                           |
| 内嵌字幕                 | hardcoded subtitles                                          | 
| 屏幕字字幕               | forced subtitles                                             |
| 无障碍音轨               | audio description                                            |

| 瑕疵                       | Artifacts                            |
| -------------------------- | ------------------------------------ |
| 色带                       | banding / color banding              |
| 锯齿                       | aliasing                             |
| 晕轮 / 振铃                | haloing / ringing                    |
| 色块                       | blocking / macroblocking             |
| 噪点                       | noise / grain [^3]                   |
| 彩色噪点 / 色度噪点        | chroma noise/grain                   |
| 静态噪点 / 静噪            | static noise                         |
| 动态噪点 / 动噪 / 时域噪点 | dynamic noise                        |
| 烂噪 / 压碎的噪点          | grain blocking / badly encoded grain |
| 烂边 / 蚊噪                | DCT ringing / DCT noise              |
| 拉丝 / 横纹                | combing                              |
| 缟缟                       | combing                              |
| 鬼影                       | blending / ghosting                  |
| 颜色越界                   | overflow and/or underflow            |
| 色度色带                   | chroma banding                       |
| 色度锯齿                   | chroma aliasing                      |
| 色度偏移                   | chroma shift                         |
| 色度溢出                   | chroma bleeding                      |
| 重复场                     | duplicated fields                    |
| 晃动                       | global motion                        |
| 彩虹                       | rainbow                              |
| 点状斑纹                   | dot-crawl                            |
| 模糊 / 糊                  | blurring                             |
| 过度柔化                   | over-blurring                        |
| 过度锐化                   | over-sharpening                      |

| 处理方法                     | Pre-processing                                 |
| ---------------------------- | ---------------------------------------------- |
| 去色带                       | de-banding                                     |
| 抖动                         | dithering                                      |
| 抗锯齿                       | anti-aliasing                                  |
| 去晕轮                       | de-ringing / de-haloing                        |
| 去色块                       | de-blocking                                    |
| 降噪                         | denoising / degrain                            |
| 亮度自适应降噪               | luma-adaptive denoising                        |
| 反交错                       | deinterlacing                                  |
| 拆场                         | field separation                               |
| 场匹配                       | field matching                                 |
| 反交卷过带                   | inverse telecine / IVTC                        |
| 去缟缟                       | de-combing                                     |
| 去鬼影                       | de-blending / ghost removal                    |
| 抗色度锯齿                   | chroma anti-aliasing                           |
| 修复晃动                     | de-pan                                         |
| 修复彩虹                     | de-rainbow                                     |
| 去除点状斑纹                 | dot-crawl removal                              |
| 纹理强化                     | texture enhancing                              |
| 锐化                         | sharpening                                     |
| 自适应锐化                   | adaptive sharpening                            |
| 保护性锐化                   | protective sharpening                          |
| 补偿性锐化                   | contra-sharpening <br> compensatory sharpening |
| 可控性锐化                   | controlled sharpening                          |
| 主动性锐化                   | active sharpening                              |
| 润线                         | line smoothing                                 |
| 收线                         | line thinning                                  |
| 描线 / 描黑                  | line darkening                                 |
| 连线                         | line connecting                                |
| 缩放                         | scaling                                        |
| 拉伸 / 拉升（分辨率）        | upscaling                                      |
| 可还原式拉升                 | revertible upscaling                           |
| 缩小（分辨率）               | downscaling                                    |
| 缩回（分辨率）               | descaling                                      |
| 还原 – 再重构 / 逆向拉伸重构 | descaling and reconstruction                   |

[^1]: 指在空间上，一幅图像中颜色（数值）变化比较平缓的部分，典型的如大块颜色填充或渐变区域，与此相对，线条边缘的数值变化是很陡峭的。

[^2]: 视频图像一般均为 YCbCr（有时习惯写为 YUV）格式，其中 Y 平面为亮度（luma）平面，Cb 和 Cr 平面为色度（chroma）平面。

[^3]: 作为画面风格的噪点是 grain，一般颗粒度较大；noise 则也可以指代瑕疵，一般可统一使用 noise。
