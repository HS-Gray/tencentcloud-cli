**Example 1: 药品说明书PDF文件结构化**

药品说明书PDF文件结构化

Input: 

```
tccli mrs DrugInstructionObject --cli-unfold-argument  \
    --PdfInfo.Base64 PDF文件Base64编码
```

Output: 
```
{
    "Response": {
        "ChemicalProductInfo": {
            "ActiveIngredient": {
                "ChemicalFormula": "HCO\r\n                           D         H-011.\r\n                                  HD\r\n                                          CH\r\n                         NH    p         H_DH\r\n                                   0=\r\n                      DH",
                "MolecularFormula": "(C15H25NO3)2C4H503",
                "MolecularWeight": "684.82",
                "Text": "主要组成成份:\r\n    本品主要成份为酒石酸美托洛尔;化学名称为:1-异丙氨基-3-[对-(2-甲氧\r\n乙基)苯氧基]-2-丙醇L(+)-酒石酸盐\r\n    化学结构式:\r\n      HCO\r\n                           D         H-011.\r\n                                  HD\r\n                                          CH\r\n                         NH    p         H_DH\r\n                                   0=\r\n                      DH\r\n    分子式:     (C15H25NO3)2C4H503\r\n    分子量:    684.82"
            },
            "AdverseReaction": {
                "Text": "不良反应的发生率约为10%，通常与剂量有关。\r\n   常见(>1/100)\r\n   一般副作用:疲劳，头痛，头晕\r\n   循环系统:肢端发冷，心动过缓，心悸\r\n   胃肠系统:     腹痛，恶心，呕吐，腹泻和便秘\r\n   少见\r\n   一般副作用:      胸痛，体重增加\r\n   循环系统:     心力衰竭暂时恶化\r\n   神经系统:     睡眠障碍，感觉异常\r\n   呼吸系统:     气急，支气管哮喘或有气喘症状者可发生支气管痉挛\r\n   罕见(<1/1000)\r\n   一般副作用:      多汗，脱发，味觉改变，可逆性性功能异常\r\n   血液系统:     血小板减少\r\n   循环系统:     房室传导时间延长，心律失常，水肿，晕厥\r\n   神经系统:梦魇       ，抑郁，记忆力损害，精神错乱，神经质，焦虑，幻觉\r\n   皮肤:   皮肤过敏反应，银屑病加重，光过敏\r\n   肝:  转氨酶升高\r\n   眼:  视觉损害，眼干和/或眼刺激\r\n   耳:  耳鸣\r\n   偶有关节痛、肝炎、肌肉疼痛性痉挛、口干、结膜炎样症状、鼻炎和注意力\r\n损害以及在伴有血管疾病的患者中出现坏疽的病例报道。"
            },
            "Appearance": {
                "Text": "本品为白色片。"
            },
            "Approval": {
                "Text": "50mg:国药准字H32025390\t\r\n25mg:国药准字H32025391"
            },
            "Brochure": {
                "Text": "(1) 25mg     (2)50mg"
            },
            "Contraindications": {
                "Text": "心源性休克。病态窦房结综合征。II、III度房室传导阻滞。不稳定的、失代\r\n偿性心力衰竭患者(肺水肿、低灌注或低血压)，持续地或间歇地接受β受体激\r\n动剂正变力性治疗的患者。有症状的心动过缓或低血压。本品不可给予心率<45\r\n次/分、P-Q间期>0.24秒或收缩压<100mmHg的怀疑急性心肌梗死的患者。伴有坏\r\n疽危险的严重外周血管疾病患者。对本品中任何成份或其它B受体阻滞剂过敏者。"
            },
            "Dosage": {
                "Text": "口服。剂量应个体化，以避免心动过缓的发生。应空腹服药，进餐时服药可\r\n使美托洛尔的生物利用度增加40%。\r\n   治疗高血压:每日100mg一200mg，分1至2次服用。\r\n   急性心肌梗死:主张在早期，即最初的几小时内使用，因为即刻使用在未能\r\n溶栓的患者中可减小梗死范围、降低短期(15天)死亡率(此作用在用药后24小时\r\n既出现)。     在已经溶栓的患者中可降低再梗死率与再缺血率，若在2小时内用药还\r\n可以降低死亡率。一般用法:可先静脉注射美托洛尔一次2.5~5mg(2分钟内)，\r\n每5分钟一次，共3次总剂量为10~15mg。之后15分钟开始口服25~50mg，每6~\r\n12小时1次，共24~48小时，然后口服一次50~100mg，一日2次。\r\n   不稳定性心绞痛:也主张早期使用，用法用量可参照急性心肌梗死。\r\n   急性心肌梗死发生心房颤动时若无禁忌可静脉使用美托洛尔，其方法同上。\r\n   心肌梗死后若无禁忌应长期使用,因为已经证明这样做可以降低心源性死亡\r\n率，包括猝死。一般一次50~100mg，一日2次。\r\n   在治疗高血压、心绞痛、心律失常、肥厚型心肌病、甲状腺功能亢                                进等症   时\r\n一般一次25~50mg，一            日2~3次，或一次100mg，一日2次。\r\n   心力衰竭:应在使用洋地黄和(或)利尿剂等抗心力衰竭的治疗基础上使用本\r\n药。起初一次6.25mg,一日2~3次，以后视临床情况每数日至一周一次增加6.25~\r\n12.5mg，一日2~3次，最大剂量可用至一次50~100mg，一日2次。\r\n   最大剂量一日不应超过300mg~400mg。"
            },
            "ExecutiveStandards": {
                "Text": "《中国药典》2020年版二部"
            },
            "GeriatricUse": {
                "Text": "老年人的药代动力学与年轻人相比无明显改变,因而老年患者用量无需调整。"
            },
            "Indications": {
                "Text": "用于治疗    高血压、心绞痛、心肌梗死、肥厚型心肌病、主动脉夹层、心律失\r\n常、甲状腺功能亢进、心脏神经官能症等。近年来尚用于心力衰竭的治疗，此时\r\n应在有经验的医师指导下使用。"
            },
            "Interactions": {
                "Text": "美托洛尔是一种CYP2D6的作用底物。抑制CYP2D6的药物可影响美托洛尔的血\r\n浆浓度。抑制CYP2D6的药物如奎尼丁、特比萘芬、帕罗西汀、氟西汀、舍曲林、\r\n塞来昔布、普罗帕酮和苯海拉明。对于服用本品的患者，在开始上述药物的治疗\r\n开始应减低本品的剂量。\r\n   本品应避免与下列药物合并使用:\r\n   巴比妥类药物:巴比妥类药物(对戊巴比妥作过研究)可通过酶诱导作用使\r\n美托洛尔的代谢增加。\r\n   普罗帕酮:4例已经使用美托洛尔的患者，在给予普罗帕酮后，美托洛尔的\r\n血浆浓度增高2~5倍，其中2例发生与美托洛尔有关的副作用。这种相互作用在\r\n8例健康志愿者中得到证实。对于这种相互作用的可能的解释是，普罗帕酮与奎\r\n尼丁相似，可通过细胞色素P4502D6途径抑制美托洛尔的代谢。由于普罗帕酮也\r\n具有β受体阻滞效应，其与美托洛尔的联合使用很难掌握。\r\n   维拉帕米:维拉帕米与β受体阻滞剂合用时(已有与阿替洛尔、普萘洛尔和\r\n吲哚洛尔合用的报道)，有可能引起心动过缓和血压下降。维拉帕米和β受体阻\r\n滞剂对于房室传导和窦房结功能有相加的抑制作用。\r\n   本品与下列药物合并使用时可能需要调整剂量:\r\n   胺碘酮:一例报道显示，同时使用胺碘酮和美托洛尔，有可能发生明显的窦\r\n性心动过缓。胺碘酮的半衰期很长(约50天)，这意味着在胺碘酮治疗停止后较\r\n长的一段时间内，使用美托洛尔仍有可能发生两药的相互作用。\r\n   I类抗心律失常药物:          I类抗心律失常药物与β受体阻滞剂有相加的负性肌力\r\n作用，故在左心室功能受损的患者中，有可能引起严重的血流动力学副作用。病\r\n态窦房结综合征和病理性房室传导阻滞的患者，也应避免同时使用美托洛尔和I\r\n类抗心律失常药物。丙吡胺和美托洛尔之间的相互作用已有明确的资料证明。\r\n   非甾体类抗炎/抗风湿药(NSAID):                 已发现NSAID抗炎镇痛药可抵消β受体阻\r\n滞剂的抗高血压作用。在这方面，经过研究的药物主要是吲哚美辛。β受体阻滞\r\n剂很可能不与舒林酸发生相互作用。在一项双氯芬酸的研究中，未发现β受体阻\r\n滞剂与双氯芬酸有相互作用。\r\n   苯海拉明:     在快速轻化代谢人群中，苯海拉明使美托洛尔通过CYP 2D6转化\r\n代谢成a-羟美托洛尔的清除降低2.5倍。美托洛尔的作用因而增强。苯海拉明可\r\n能抑制其它   CYP2D6底物的代谢。\r\n   地尔硫草:     钙离子拮抗剂和β受体阻滞剂对于房室传导和窦房结功能有相加\r\n的抑制作用。     已经有β受体阻滞剂与地尔硫草合并使用时发生明显心动过缓的病\r\n例报道。\r\n   肾上腺素:     约有10例报道显示，接受非选择性β受体阻滞剂(包括吲哚洛尔\r\n和普萘洛尔)治疗的患者，在给予肾上腺素后发生明显的高血压和心动过缓。这\r\n些临床   观察结果   已经在对健康志愿者的研究中得到证实。局部麻醉药中的肾上腺\r\n素在血管内给药时有可能引起这种反应。根据推测，使用心脏选择性的β受体阻\r\n滞剂时，    发生这种反应的危险性较低。\r\n   苯丙醇胺:     苯丙醇胺50mg单剂给药能使健康志愿者的舒张压升高到病理的水\r\n平。普萘洛尔通常能         拮抗  这种由苯丙醇胺引起的血压增高。但是在接受大剂量苯\r\n丙醇胺   治疗的   患者中，    β受体阻滞剂可反常地引起高血压反应。在单独使用苯丙\r\n醇胺治疗的过程中，也有发生高血压反应的报道。\r\n   奎尼丁:   奎尼丁在所谓的快速羟化者(该类型在瑞典超过90%)中可抑制\r\n美托洛尔的代谢，结果使后者的血浆浓度显着升高、β受体阻滞作用增强。其他\r\n经由同一酶解途径(细胞色素P450 2D6)进行代谢的β受体阻滞剂，也可能会与奎\r\n尼丁发生同样的相互作用。\r\n   可乐定:    β受体阻滞剂有可能加重可乐定突然停用时所发生的反跳性高血压。\r\n如欲终止与可乐定的联合治疗，应在停用可乐定前数日停用β受体阻滞剂。\r\n   利福平:    利福平可诱导美托洛尔的代谢，导致后者的血药浓度降低。\r\n   应严密监控同时接受其它β受体阻滞剂(如:滴眼液)或单胺氧化酶(MAO)抑\r\n制剂的患者。在接受β受体阻滞剂治疗的患者，吸入麻醉会增加心脏抑制作用。\r\n   接受β受体阻滞剂治疗的患者应重新调整口服降糖药的剂量。若与西咪替丁\r\n或肼屈嗪合用，美托洛尔的血浆浓度会增加。"
            },
            "Manufacturer": {
                "Address": "泰州市药城大道88号",
                "PostalCode": "225300",
                "Text": "委托方企业名称:阿斯利康制药有限公司\t\r\n注册地址:无锡市新区黄山路2号\t\r\n邮政编码:214028\t\r\n受托方企业名称:阿斯利康药业(中国)有限公司\t\r\n生产地址:泰州市药城大道88号\t\r\n邮政编码:225300\t\r\n质量投诉电话:4008281755,800 8281755\t\r\n产品信息免费咨询电话:400 820 8116,800 820 8116\t\r\n传真:021-38723255\t\r\n网址:www.astrazeneca.com.cn\t\r\n\r\n                                                    AstraZeneca\r\n                                                                   2003-2020\r\n                            BETALOC和倍他乐克是AstraZeneca公司的商标。\r\n                                                       AstraZeneca",
                "Website": "www.astrazeneca.com.cn\t\r\n\r\n                                                    AstraZeneca\r\n                                                                   2003-2020\r\n                            BETALOC和倍他乐克是AstraZeneca公司的商标。\r\n                                                       AstraZeneca"
            },
            "Name": {
                "BarndName": "倍他乐克",
                "EnName": "MetoprololTartrate Tablets",
                "GenericName": "酒石酸美托洛尔片",
                "Pinyin": "Jiushisuan Meituoluoer Pian",
                "Text": "通用名称:      酒石酸美托洛尔片\r\n    商品名称:      倍他乐克\r\n    英文名称:    MetoprololTartrate Tablets\r\n    汉语拼音:    Jiushisuan Meituoluoer Pian"
            },
            "Overdose": {
                "Text": "毒性:   美托洛尔7.5g引起成人致死性中毒。一例5岁儿童误服100mg经洗胃后\r\n无任何症状。12岁儿童给予450mg引起中度中毒，成人给予1.4g引起中度中毒、\r\n给予2.5g引起重度中毒、给予7.5g引起极重度中毒。\r\n   症状:   心血管系统症状最为显着，但某些病例，特别是儿童和年轻患者，可\r\n能以中枢神经系统症状和呼吸抑制为主要表现。主要的中毒症状有心动过缓、I~\r\nIII度房室传导阻滞、心搏停止、血压下降、外周循环灌注不良、心功能不全、\r\n心源性休克、呼吸抑制和窒息。其他症状包括疲乏、精神错乱、神志丧失、频细\r\n震颤、痉挛、出汗、感觉异常、支气管痉挛、恶心、呕吐、可能有食管痉挛、低\r\n血糖(儿童特别容易发生)或高血糖症、高钾血症，对肾脏的影响，以及一过性\r\n肌无力综合征。合并酒精，抗高血压药、奎尼丁或巴比妥类药物可能加重患者的\r\n病情。药物过量的首发症状可见于服药后20分钟至2小时。\r\n   治疗:   诊断明确者，给予洗胃和活性炭，并严密观察病情变化。注意!为减\r\n少迷走神经刺激的危险，洗胃前应先静脉给予阿托品(成人0.25~0.5mg，儿童\r\n10~20μg/kg)。有指征时，进行气管内插管和呼吸支持治疗。给予适当的容量\r\n替代治疗，输注葡萄糖，监测心电图。阿托品1.0~2.0mg静脉注射，必要时可重\r\n复注射(主要控制迷走神经症状)。对心肌功能抑制的患者，可滴注多巴酚丁胺\r\n或多巴胺，葡乳醛酸钙(9mg/ml)10~20ml。另一种替代方法是胰高血糖素50~\r\n150μg/kg，1分钟内静脉注射，继以静脉滴注，或用氨力农。部分患者加用肾上\r\n腺素有效。QRS波增宽和心律失常的患者，可输注氯化钠或碳酸氢钠。可能需要\r\n安装心脏起搏器。对心搏骤停的患者，有时需要长达数小时的复苏抢救。治疗支\r\n气管痉挛时，可使用特布他林(注射或吸入)。此外，进行对症治疗。"
            },
            "Packaging": {
                "Text": "铝塑泡包装;\r\n25mg:20片/板/盒，20片/板x2板/盒，20片/板x3板/盒;\r\n50mg:20片/板/盒,20片/板x2板/盒;"
            },
            "PediatricUse": {
                "Text": "儿童使用本品的经验有限。"
            },
            "Pharmacokinetics": {
                "Text": "本品的生物利用度为40-50%。在服药后1-2小时达到最大的β受体阻滞作用。\r\n每日一次口服100mg后，对心率的作用在12小时后仍显着。美托洛尔主要在肝脏\r\n由CYP2D6代谢，三个主要的代谢物已被确定，均无具有临床意义的β受体阻滞作\r\n用。血浆半衰期为3-5小时。约5%的美托洛尔以原形由肾排泄，其馀的均被代谢。"
            },
            "PharmacologyToxicology": {
                "Text": "美托洛尔是一种选择性的β受体阻滞剂，其对心脏β受体产生作用所需剂\r\n量低于其对外周血管和支气管上的β:受体产生作用所需剂量。随剂量增加，β\r\n受体选择性可能降低。\r\n   美托洛尔无β受体激动作用，几乎无膜激活作用。β受体阻滞剂有负性变力\r\n和变时作用。\r\n   美托洛尔的治疗可减弱与生理和心理负荷有关的儿茶酚胺的作用,降低心率、\r\n心排出量及血压。在应激状态下，肾上腺分泌的肾上腺素增加，美托洛尔不会妨\r\n碍正常的生理性血管扩张。在治疗剂量，美托洛尔对支气管平滑肌的收缩作用弱\r\n于非选择性的β受体阻滞剂，该特性使之能与β受体激动剂合用，治疗合并有支\r\n气管哮喘或其他明显的阻塞性肺病的患者。美托洛尔对胰岛素释放及糖代谢的影\r\n响小于非选择性β受体阻滞剂，因而可用于糖尿病患者。与非选择性β受体阻滞\r\n剂相比，美托洛尔对低血糖的心血管反应如心动过速的影响较小，血糖回升至正\r\n常水平的速度较快。\r\n   对于高血压患者，本品可明显降低直立位、平卧位及运动时的血压，作用持\r\n续24小时以上。美托洛尔治疗开始时可观察到外周血管阻力的增加，然而，长期\r\n治疗获得的血压下降可能是由于外周血管阻力下降而心排出量不变。对于男性中\r\n/重度高血压患者，美托洛尔可降低心血管病死亡的危险。美托洛尔不会引起电\r\n解质紊乱。\r\n   对快速型心律失常的患者，本品可阻断交感神经活性增加的作用，使心率减\r\n慢。这主要通过降低起搏细胞的自律性，及延长室上性传导时间来实现。\r\n   本品显示快速有效的缓解甲状腺毒症的症状。高剂量的美托洛尔可降低升高\r\n的T3值。T4水平不受影响。\r\n   美托洛尔可减少再次心肌梗死的危险,减少心源性死亡特别是心肌梗死后猝\r\n死的危险。"
            },
            "Precautions": {
                "Text": "肾功能损害\r\n   肾功能对本品清除率无明显影响，因此肾功能损害患者无需调整剂量。\r\n   肝功能损害\r\n   通常肝硬化患者所用美托洛尔的剂量与肝功能正常者相同。仅在肝功能非常\r\n严重损害(如旁路手术患者)时才需考虑减少剂量。\r\n   接受β受体阻滞剂治疗的患者不可静脉给予维拉帕米。\r\n   美托洛尔可能使外周血管循环障碍疾病的症状如间歇性跛行加重。对严重的\r\n肾功能损害、伴代谢性酸中毒的严重急症，及合用洋地黄时，必须慎重。\r\n   在没有伴随治疗的情况下,本品不可用于潜在的或有症状的心功能不全的患\r\n者。患变异型(Prinzmetal氏)心绞痛的患者，在使用β受体阻滞剂后可能会由于\r\na受体介导的冠状血管收缩而导致心绞痛发作的频度和程度加重。因此，非选择\r\n性β受体阻滞剂不能用于此类患者。选择性β受体阻滞剂在使用时也必须慎重。\r\n   对支气管哮喘或其他慢性阻塞性肺病患者,应同时给予足够的扩支气管治疗，\r\nβ受体激动剂的剂量可能需要增加。\r\n   美托洛尔的治疗对糖代谢的影响或掩盖低血糖的危险低于非选择性β受体\r\n阻滞剂。\r\n   在罕见的情况下,原有的中度房室传导异常可能加重(可能导致房室阻滞)。\r\n   β受体阻滞剂的治疗可能会妨碍对过敏反应的治疗,常规剂量的肾上腺素治\r\n疗并不总能得到预期的疗效。嗜铬细胞瘤患者若使用本品，应考虑合并使用α受\r\n体阻滞剂。\r\n   本品应尽可能逐步撤药，整个撤药过程至少用二周时间，剂量逐渐减低，直\r\n至最后减至25mg(50mg片的半片)。在此期间，特别是对于已知伴有缺血性心脏\r\n病的患者应进行密切监测。在撤除β受体阻滞剂期间，可能会使冠状动脉事件，\r\n包括心脏猝死的危险增加。\r\n   在手术前应告知麻醉医师患者正在服用本品。对接受手术的患者，不推荐停\r\n用β受体阻滞剂。\r\n   对驾驶汽车和操作机械的影响\r\n   在用本品治疗过程中可能会发生眩晕和疲劳，因此在需要集中注意力时，如\r\n驾驶和操作机械时应慎用。\r\n   运动员慎用"
            },
            "PregnancyLactationUse": {
                "Text": "β受体阻滞剂(包括美托洛尔)会减少胎盘灌注，可引起胎儿发育迟缓、心\r\n动过缓、宫内死亡、流产及早产。\r\n   美托洛尔在人乳中浓度很高(大约相当于母体血浆浓度的三倍)。β受体阻\r\n滞剂(包括美托洛尔)可对新生儿和婴儿产生不利影响，尤其是心动过缓。\r\n   除非必要，美托洛尔不得用于孕妇或哺乳期妇女。\r\n   妊娠、哺乳期妇女不宜使用本品。\r\n   如果你已经妊娠或正在哺乳期间、可能妊娠或试图怀孕，应在使用本品前咨\r\n询医生。"
            },
            "Storage": {
                "Text": "避光、密封保存。"
            },
            "ValidityPeriod": {
                "Text": "36个月"
            }
        },
        "RequestId": "108e3fa2-355b-4c1e-adfd-08557bbbc6ec"
    }
}
```
