# VCB-Studio 术语对照表

本术语对照表为发布组翻译制作吐槽提供参考。

添加条目时请归入对应表格。如果需要添加额外备注，请使用脚注。

下列对应翻译均取自 [VCB-Studio 科普教程 6]( https://vcb-s.com/archives/4738 ) 或以往翻译惯例，特定场合下的翻译应与总监商讨。

如无特殊标记，英文词性均为名词。

| 一般词汇           | General                         |
| ------------------ | ------------------------------- |
| 原盘               | Original source                 |
| 画风               | Image style                     |
| 线条               | Line / Line-art                 |
| 纹理               | Texture                         |
| 暗场               | Dark area                       |
| 平面               | Plane / Flat area<sup name="a1">[1](#f1)</sup>          |
| 码率               | Bit-rates                       |
| 参数               | Parameters                      |
| 还原度             | Revivification                  |
| 压制               | Encoding                        |
| 原生分辨率         | Native resolution               |
| 轻微 / 适当 / 较强 | (adj.) Mild / Moderate / Strong |
| 算法               | Algorithm                       |

<b name="f1">1</b> Plane 一般搭配前置定义词，例如色度平面 Chroma plane；单独的平面可以说 Flat area。[↩](#a1)

| 瑕疵                | Artifacts                     |
| ------------------- | ----------------------------- |
| 色带                | Banding / Colour banding      |
| 锯齿                | Aliasing                      |
| 晕轮 / 振铃         | Ringing / Haloing             |
| 色块                | Blocking / MacroBlock         |
| 噪点                | Noise / Grain<sup name="a1">[2](#f2)</sup>             |
| 彩色噪点 / 色度噪点 | Chroma noise / grain          |
| 烂边 / 蚊噪         | DCT ringing  / DCT noise      |
| 拉丝 / 横纹 / 交错  | Interlacing                   |
| 缟缟                | Combing                       |
| 鬼影                | Blending / Ghosting           |
| 颜色越界            | (Chroma) Overflow / Underflow |
| 色度色带            | Chroma banding                |
| 色度锯齿            | Chroma noise / grain          |
| 色度偏移            | Chroma shift                  |
| 色度溢出            | Chroma bleeding               |
| 重复场              | Duplicate field               |
| 晃动                | Global motion / Pan           |
| 彩虹                | Rainbow                       |
| 点状斑纹            | Dot-crawl                     |
| 过度柔化            | Over blurring                 |

<b name="f2">2</b> 作为画风特点的噪点是 Grain，作为瑕疵的噪点是 Noise，不确定时可统一使用 Noise。[↩](#a2)



| 处理方法       | Pre-processing                                 |
| -------------- | ---------------------------------------------- |
| 去色带         | De-banding                                     |
| 抗锯齿         | Anti-aliasing                                  |
| 去晕轮         | De-ringing / De-haloing                        |
| 去色块         | De-blocking                                    |
| 降噪           | De-noising / De-grain                          |
| 反交错         | De-interlacing                                 |
| 场匹配         | Field-matching                                 |
| 反交卷过带     | Inverse Telecine (IVTC)                        |
| 去缟缟         | De-combing                                     |
| 去鬼影         | De-blending / Ghost removal                    |
| 修复颜色越界   | Fix overflow / underflow                       |
| 处理色度锯齿   | Chroma anti-aliasing                           |
| 修复色度偏移   | (v.) Fix chroma shift                          |
| 修复色度溢出   | (v.) Fix chroma bleeding                       |
| 解决重复场     | (v.) Fix duplicate field                       |
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
| 拉升（分辨率） | Upscaling                                      |
| 可还原式拉升   | Revertible upscaling                           |
| 缩回（分辨率） | Downscaling                                    |
| 还原 – 再重构  | Downscaling and reconstruction                 |
