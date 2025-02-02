from volcenginesdkarkruntime import Ark
import time

# 豆包模型 ep-20241220102344-rcmq5  Doubao-vision-lite-32kDoubao-vision-lite-32k
client = Ark(
    base_url="https://ark.cn-beijing.volces.com/api/v3",
)
start_time = time.time()
# Non-streaming:
print("----- standard request -----")
completion = client.chat.completions.create(
    model="ep-20241220102344-rcmq5",
    messages = [
        {"role": "system", "content": "你现在是流程审批人员，需要关注合同的信息和发票金额"},
        {"role": "user", "content": r"""我现在是审批人员,需要审批合同信息和发票金额是否一致，此发票为合同的第5支付节点，为部分支付金额，一年免费运维期满后支付的金额，发票内容为：备
注
开票人：
24422000000177182575
2024年12月03日
武汉市汉阳市政建设集团有限公司
914201054413664384武汉汇科智创科技有限公司
91420105MA49MQT249
¥85021.89 ¥5101.31
玖万零壹佰贰拾叁圆贰角整 ¥90123.20
张美琪
张美琪*信息技术服务 *软件开发
服务6% 85021.89 5101.31
购方开户银行 :中国农业银行武汉汉阳支行 ;    银行账号 :17024201040006823;
销方开户银行 :中信银行股份有限公司武汉汉阳支行 ;    银行账号 :8111501012500798330;
工程名称：流程中台项目 ;
收款人:张迪;    复核人:刘子玉;，合同内容为:，
         流程中台项目
软件开发合同












武汉市汉阳市政建设集团有限公司
 2023年 07 月 18  日

软件开发合同
甲方（委托人）： 武汉市汉阳市政建设集团有限公司
乙方（受托人）： 武汉汇科智创科技有限公司
根据《中华人民共和国民法典》的规定，在公平、诚实、信用的基础上，经充分沟通和友好协商，甲方委托乙方进行软件项目的开发工作，包括部署上线、功能优化、数据接口等系统开发服务、培训上线等服务。为了规范双方在此项目上的权利和义务，在《中华 
人民共和国民法典》的原则指导下，订立本协议，本协议由基本条款及附件组成，由双方共同遵守。

第一条  定义和解释
1、定义。在本合同中，除非上下文另有规定，下列术语具有如下含义：
（1）“软件”包括“软件系统”，除另有指明外，指在本协议履行期内所开发和提供的当前、将来的软件版本及相关的文件。
（2）“交付”指乙方在双方规定的日期内交付约定开发的软件的行为。
（3）“规格”是指在技术或其他开发任务上所设定的技术标准、规范。
（4）“源代码”指用于该软件的全部源代码。其必须能够被第三方软件公司的程序员理解和使用，可打印、被机器阅读或具备其他合理而必要的形式，包括对该软件的评估、测试或其他技术文件。
（5）“服务”指根据协议规定乙方应承担的技术支持，包括但不限于需求调研、方案设计、产品设计、虚拟环境部署、开发、测试、维护、培训、咨询等服务。
（6）“技术文档”指为满足软件产品的使用、二次开发、升级和维护的需要，乙方在本合同项下需向甲方提供的相关文档以及经双方协商一致的需向甲方提供的相关文档；
（7）“知识产权”指权利人对其所创作的智力劳动成果所享有的专有权利，无论上述权利根据任何适用法律产生，包括所有因侵犯或侵占任何上述权利而产生的权利或诉因；
2、解释。除非清楚地表明相反意思或上下文另有规定，在本合同以及任何其他合同文件中：
（1）若付款日适逢非工作日，则顺延至次一个工作日付款；
（2）本合同之附件为本合同之一部分；
（3）本合同经双方协商订立，不得因一方起草了本合同或其任何条款，而按照不利于该方的原则来解释合同条文。

第二条  合同内容
乙方负责开发流程中台各项功能，建设内容如下：
2、乙方负责集成系统与流程中台对接的改造开发，并保证集成系统与流程中台的对接功能完整。
3、乙方应分别交付试运行、正式两套系统，并部署至甲方的试运行环境及正式环境，同时两套系统均需与甲方的相关集成系统集成完成。系统功能以本合同开发内容为基准，如甲方要求变更的内容不在此范围内或对原建设内容进行修改，则明确为需求变更。    
4、总进度计划

5、性能设计要求
5.1 乙方要保证系统的可用性，确保系统可用性达到  99%  ，即每年的停服时间应小于  87.6  小时；每次影响使用的停服时间最长不超过  1  个小时；确保发生故障后系统平均恢复时间小于  30  分钟；非乙方导致的停服除外。
5.2 乙方要保证系统性能满足如下要求:在当前页面的同时访问用户数为  300   的情况下，一般页面响应时间小于  3  秒，复杂页面响应时间小于  5  秒，报表类型页面响应时间小于  10  秒，接口QPS 大于  300  次/秒。超过访问用户数指标,即当前页面的 
同时访问数超过  300  的情况下，要求系统处于可用状态、且满足上面描叙指标，系统响应时间为小于  10  秒。
5.3 乙方运维服务期内，产品的后期使用过程中，因乙方原因导致性能不满足要求，乙方需无偿解决性能问题，乙方需及时响应且不超过  30  天解决问题。若乙方逾期都无法达到约定的性能要求，乙方应承担违约责任，处以逾期性能不达标罚款  1000  元/天。
若交付产品的后期使用过程中数据运行要求和可靠性要求一直不达标，甲方有权追责，处以合同总金额的  20%  作为违约赔偿。
6、技术设计要求
（1）乙方需要满足系统设计要求，包含系统架构、部署架构、核心流程、开源软件版本标准等内容，系统设计要求的内容参照附录4-技术设计要求清单：《系统技术设计要求》。
（2）乙方需要满足的后端开发技术规范，包含数据库设计规范、编程规范、系统安全规范、项目代码结构规范等内容，后端开发技术规范的内容参照附录4-技术设计要求清单：《后端开发技术要求》。
（3）乙方需要满足的前端开发技术规范，包含前端编程规范、代码结构规范等，前端开发技术规范的内容参照附录4-技术设计要求清单：《前端开发技术要求》。
（4）乙方需要满足的接口交互技术规范，包含接口定义、接口参数定义、接口返回数据结构定义、接口状态码定义等内容，接口交互技术规范的内容参照附录4-技术设计要求清单：《接口交互设计要求》。
7、集成设计要求
甲方为规划企业信息化建设整体一张图，消除数据孤岛，乙方应积极配合甲方进行该项目的应用集成和数据集成。与甲方系统集成要求如下：
7.1 乙方应积极配合与甲方的主数据系统集成，保证获取数据的准确性、及时性及安全性，未经甲方授权，数据不能泄露给其他三方，如发生数据泄露事故，甲方有权利追责，并处以相应损失的罚款。对接的主数据的数据域有:  组织、人员、岗位、角色、系统分
类，流程分类、流程组织、基础字典  。如乙方因集成有额外费用，应在合同内明确。
7.2 乙方应积极配合与甲方的门户中心系统集成，保证对接功能的完整性和安全性，门户中心对接的功能有：  登录中心  。如乙方因集成有额外费用，应在合同内明确。
7.3  乙方应积极配合与甲方的BPM系统集成，BPM是甲方管理企业所有业务活动的监管系统，乙方需要将该项目系统内所有涉及到业务活动的状态变更通过接口同步至甲方BPM系统，且保证数据的准确性、及时性及安全性，未经甲方授权，数据不能泄露给其他三方 
，如发生数据泄露事故，甲方有权利追责，并处以相应损失的罚款。如乙方因集成需收取额外费用，应在合同内明确。
7.4 乙方应积极配合与甲方的数据分析系统集成，乙方需要保证数据的开放性、可访问性、准确性及信息安全，保证该软件产品原始数据可作为数据源接入到甲方的数据分析系统中，不能以该软件产品信息数据加密或其他原因为原由，拒不支持甲方的数据分析系 
统的集成与对接。如乙方因集成有额外费用，应在合同内明确。

第三条  合同金额
1、本项目费用总计人民币  901232.00  元（人民币大写 玖拾万壹仟贰佰叁拾贰圆整），含  6  %的增值税，不含税金额为人民币  817200.00  元（人民币大写 捌拾壹万柒仟贰佰圆整  ），税款为人民币   49032.00  元（人民币大写  肆万玖仟零叁拾贰圆整 
）。其中费用构成如下：
（1）基础平台开发费用：  866232.00  元（大写：捌拾陆万陆仟贰佰叁拾贰圆整），税率  6%  。
（2）部署服务租赁费用：  35000.00  元（大写：叁万伍仟圆整），税率  6%  。
如遇国家税务政策变化导致乙方增值税税率发生变化时，本合同未执行完的合同价格按除税价不变的原则进行调整。款项支付前，乙方须先向甲方提供相应金额的增值税专用发票；乙方未提供或提供不符合甲方要求的票据，甲方有权延期支付款项并不视为违约； 
甲方在收到增值税专用发票后，2周内以银行转账方式支付。
本合同附件1价格清单包括乙方所有成本、利润、保险、税金等，对于没有填入单价或合价的细目，其费用应视为已包括在本合同价格清单的其他单价或合价中。
2、本合同金额涵盖所有与该合同相关的工作、产品和服务。除产品功能设计变更外，其他合同相关的无论明示或暗示，无论合同中是否有明确提及，都应视为已经包含在合同金额之内。
本项目软件系统进入开发阶段后，如因甲方需求变更导致乙方产生额外成本，乙方应与甲方签订需求变更单，由甲乙双方签字确认工时数量，按照标准开发人员  1200  元/天（为综合含税单价，税率为  6%  的增值税）额外计算变更费用。
第四条  结算及支付方式
1、合同费用支付时间、具体核算方式及金额如下：
在项目结算阶段，应严格参照上述表格里的支付条件及相应的支付比例进行结算。乙方为甲方提供软件服务及合同履行过程中产生的其他费用均由乙方自行承担，乙方应对合同内容里所有要求履约。
在项目的各项支付节点前，乙方须先向甲方提供相应金额的增值税专用发票及支付条件里的相关材料；乙方未提供或提供不符合甲方要求的票据或材料，甲方有权延期支付款项并不视为违约；甲方在收到增值税专用发票及材料后，2周内以银行转账方式支付。    
    如项目发生合同约定金额之外的变更费用，则在第4、5支付节点结算时，乙方额外还需提供所有的需求变更单并汇总所有需求变更费用至软件项目结算单里进行项目结算。
2、乙方银行信息
开户名称：   武汉汇科智创科技有限公司
开户银行：   中信银行汉阳支行
银行账号：   8111501012500798330
3、甲方银行信息
开户名称：   武汉市汉阳市政建设集团公司
开户银行：   中国农业银行武汉汉阳支行
银行账号：   914201054413664384
地    址：   武汉市汉阳区金龙公馆18楼
第五条  项目完成时间、验收标准和验收方式
1、项目起止时间： 2023年3月15日  -  2023年11月20日  （实际开始日期以合同签订时写明的日期为准，若签订时间延期，完成时间顺延）。
2、本项目开发内容需要通过试点项目集成应用验收成果，需要乙方完成试点项目的部署后，向甲方发起书面试运行启动通知并出具内部通过的测试报告，进入试运行期，试运行期限为  2  个月。在试运行期间，乙方应分别在甲方的试运行环境及正式环境分别部 
署验证，各环境验证均不得少于  15  天。甲方按照本合同开发内容对每个功能点创建试运行数据。甲方如果发现软件产品有缺陷，或性能和质量不符甲方要求时，乙方有责任对其进行修改和更正。同时试运行期依据上述修改、更正期间进行相应顺延。试运行期 
满后，如甲方未提出异议，则视为试运行完成。
3、试运行完成，启动正式运行。稳定运行  30  个工作日后，乙方将书面向甲方发起验收确认。甲方依据功能清单、建设方案、原型设计及合同文件对项目是否满足功能实现进行验收。验收标准除完成合同第二条里约定的开发内容外，乙方还应提供满足本条开发
交付要求里的相关交付物。如甲方验收后发现存在不达标情况，甲方可书面反馈给乙方，双方协商处理；如甲方验收后不存在问题，乙方准备项目验收报告及需要提供的文档报甲方组织验收会，甲乙双方签字确认后完成验收。若乙方发起验收后  30  个工作日甲 
方未回复，则视为默认验收通过。
4、开发交付要求：
4.1 乙方负责提供产品各角色操作文档及视频教程，内容容易理解, 并通过使用适当的术语、图形、流程图、详细的解释来表达，格式和标准参照附录3-项目验收交付清单：《系统操作文档》。
4.2 乙方负责提供软件设计说明书PRD文档（包括但不限于全局说明、版本更新说明、完整功能清单、总体流程、各子模块详细设计、交互文档及子流程）及全套效果图，格式和标准参照附录3-项目验收交付清单：《产品需求说明书》。
4.3 乙方负责提供应用系统的接口文档，包括接口的参数信息、返回值信息、错误码信息等，确保接口文档的清晰性、完整性。接口文档的格式和标准参照附录3-项目验收交付清单：《接口说明文档》。
4.4 乙方负责提供项目相关的开发资料和培训指导，确保开发资料的清晰性和完整性，确保甲方开发人员具有基于源代码进行二次开发的能力。开发资料的格式和标准参照附录3-项目验收交付清单：《组件集成文档》。
4.5 乙方负责提供架构图设计文档，包含业务架构图、应用架构图、技术架构图、数据架构图，格式和标准参照附录3-项目验收交付清单:《架构图设计文档》。（必要）
4.6 乙方负责提供应用系统的数据库设计文档，包含表信息、表关系信息、表的字段信息，确保其完整性、准确性。设计文档建议采用PowerDesigner软件设计。数据库设计文档格式和标准参照附录3-项目验收交付清单：《数据库设计文档》。（必要）
4.7 乙方负责提供项目相关的开发资料和培训指导，确保开发资料的清晰性和完整性，确保甲方开发人员具有基于源代码进行二次开发的能力。开发资料的格式和标准参照附录3-项目验收交付清单：《开发说明文档》。（建议）
4.8 乙方负责提供应用部署相关文档，确保甲方能独立完成应用系统的部署。系统部署文档内容包含系统部署架构图、安装环境要求、安装部署的详细步骤、应用安装的配置说明、常见故障诊断的处理方法等。系统部署文档的格式和标准参照附录3-项目验收交付 
清单：《系统部署文档》。（必要）
4.9 乙方负责提供的系统功能测试报告，确保功能测试场景全覆盖，保证测试结果的真实性。系统功能测试报告格式和标准参照附录3-项目验收交付清单：《系统功能测试报告》。（必要）
4.10 乙方负责提供的系统性能测试报告，确保系统交付标准满足甲方所提出的性能指标，保证测试结果的真实性。系统性能测试报告格式和标准参照附录3-项目验收交付清单：《系统性能测试报告》。（必要）
第六条  甲方的权利和义务
1、在乙方按照合同约定履行相应义务的前提下，按本合同约定支付费用。甲方未按时支付开发费用的，每迟延支付一周，应按合同总金额的【0.1】%向乙方支付违约金。甲方由此累计支付的违约金最高不超过合同总金额的【10】%。
2、甲方有权要求乙方按时完成本合同约定的软件开发任务，甲方有权监督乙方工作进度和质量，乙方人员在甲方办公场所办公的，有权对乙方工作人员进行必要的管理。
3、本项目软件系统进入部署及验收阶段之前，甲方可以变更或新增委托项目内容、规模、条件，或对所提供资料做出实质性修改。乙方应对甲方提出的需求做出评估，如因甲方的变更或新增内容严重影响开发周期的，双方协商一致后可对开发周期予以延长。    
4、甲方有权根据本项目软件系统的工作内容和成果要求，对乙方项目组主要成员的构成提出合理的要求。在合同履行过程中，甲方如发现乙方项目组主要成员有损害甲方利益的行为的，可以要求乙方替换项目组主要成员，乙方在收到甲方提出的人员更换要求后，
应在五个工作日内对人员进行替换。
5、甲方应当指定专人负责在合理的时间内依据本项目实际需要向乙方提供本项目软件开发有关资料，及时响应乙方的有关需求并进行相关的协调工作。若因甲方响应不及时导致的延期，本项目整体时间顺延。
6、本项目的软件系统具备验收条件时，甲方应对照第五条验收标准进行验收。如发现不符合约定需要修改的，应当明确修改的要求和期限。
7、甲方应对软件项目所用的用户名、登录密码等信息自行采取保密措施，承担保密义务和责任。由于甲方账户管理不善所产生的一切后果由甲方承担。 
8、本项目软件系统验收完成后，若甲方需要对功能进行修改或增加新功能，可要求乙方开发相应功能，并根据甲乙双方签署确认的工时数量，结合第三条合同条款中约定的软件系统开发期间标准开发人员人天单价进行费用计算。同时签署补充协议合同对开发的内
容、费用、支付进行规定。

第七条  乙方的权利和义务
1、按照甲方提供的资料及本合同约定的要求完成项目实施，乙方向甲方提供明确详细的实施需求资料，如在项目实施过程中需变更需求，应书面报甲方确认，在取得甲方确认后方可变更。具体工作与要求详见本合同约定的条款及双方签署的相关文件。
2、乙方应按照本合同确认的内容提供技术服务，在提供服务过程中，根据甲方的要求及时修改方案，确保按期并高质量地提供技术服务成果。
3、当甲方未及时提供软件开发所需信息，乙方有权向甲方提出延期要求，延期时间由双方协商确定。
4、乙方应按照有关法律法规、设计标准、行业技术规范以及本合同约定的工作内容、技术标准、工作进度和成果要求进行全过程的管理。根据本合同约定，制定项目实施总体计划和各实施阶段的详细工作计划，并按工作进度向甲方交付成果。
5、本项目软件系统验收时，除完成合同约定的开发内容外，乙方还需参考合同第五条的验收标准向甲方提供交付物。
6、在本合同约定的项目验收合格后，乙方应根据甲方的需求对甲方人员进行一次免费培训。
7、如因乙方原因，未按照约定的时间提交可交付成果物，每迟延交付一周，应按合同总金额的【0.1】%向甲方支付违约金。乙方由此累计支付的违约金最高不超过合同总金额的【10】%。
8、如乙方欲使用甲方的名称、商标、域名、企业标志用于客户介绍等，乙方需取得甲方同意，且承诺此使用不能损害甲方的利益。如发生损害甲方利益的行为，甲方有权利进行追责。

第八条  违约责任
 1.在本合同履行过程中，任何一方的行为违背了本协议的规定，致使本合同不能继续履行，受损害一方可立即以书面形式通知违约方终止本协议。
2.在相关法律所允许的最大范围内，任何一方均不就另一方附带、间接的、偶然的以及利润和商业机会的损失承担责任。

第九条  保密义务
1、在本合同履行期间及履行完毕后的任何时候，任何一方均应对因履行本合同从对方获取或知悉的保密信息承担保密责任，未经对方书面同意不得向第三方透露，否则应赔偿由此给对方造成的全部损失。
2、保密信息指任何一方因履行本合同所知悉的任何以口头、书面、图表或电子形式存在的对方信息，具体包括：
（1）任何涉及对方过去、现在或将来的商业计划、规章制度、操作规程、处理手段、财务信息；
（2）任何对方的技术措施、技术方案、软件应用及开发，硬件设备的品种、质量、数量、品牌等；
（3）任何对方的技术秘密或专有知识、文件 、报告、数据、客户软件、流程图、数据库、发明、知识及贸易秘密。
无论上述信息是否享有知识产权。
3、如需要，双方应根据相应的要求签署相应的保密协议，保密协议与本条款存在不一致的，以保密协议为准。本条款不因合同变更、修改、解除而失效。

第十条  知识产权
1、乙方保证其提供的软件产品未侵犯第三人之著作权、商标权、专利权等知识产权，不会侵犯任何第三人的商业秘密或对任何第三人构成不正当竞争，如因此与第三人形成争议、诉讼或仲裁案件，由乙方承担全部责任和费用，并负责赔偿甲方由此而遭受的全部损
失。同时乙方需提供全力支持防止因上述侵权给甲方带来的直接损失，包括但不限于提供甲方继续使用本合同项下的软件而需取得的第三方授权、修改本合同项下软件使其至少在功能上可以替代原技术、提供功能上相等的使甲方可以达到原合同目的的其他软件， 
并承担因此而产生的所有的费用。
2、如乙方经营不善发生注销倒闭情况，乙方无偿向甲方提供本系统的全部源代码，包含基础平台底层源码及应用层源码。
3、乙方应保证履行本合同过程中的全部研究成果合法，并不得损害任何第三人合法权益，包括但不限于第三人著作权、专利权、商标权等知识产权和其他合法权益。
4、 乙方履行本合同形成的，包括但不限于软件系统文档，源代码等，按照集团公司要求，所有知识产权信息归属汉阳市政集团公司，暂由汇科智创公司保管。

第十一条  系统维护服务
1、本合同本项目系统软件的免费维护期为  1  年。免费维护期自验收通过之日起计算。
2、乙方所提供的应用系统在使用期间，如果存在系统缺陷或者漏洞，乙方应及时响应，无偿紧急修复漏洞，要求系统阻断性缺陷不超过  12  小时解决，系统一般性缺陷不超过  48  小时解决，特殊情况在取得甲方同意的情况下不超过  10  天解决。若乙方逾期
都无法解决相应问题，乙方应承担相应责任，处以逾期罚款  1000  元/天，若应用系统在使用期间,系统缺陷或者漏洞一直没有修复，甲方有权追责，处以合同总金额的  20%  作为违约赔偿。
3、在免费维护期到期后，从第二年开始，每年以合同额里的开发费用的  6%  作为运维年费（不包含部署服务租赁费用），每年运维服务标准应按照当前合同运维服务内同条款约定执行。
4、在后期服务中，如甲方提出的需求不符合运维服务内容，且需要乙方投入成本的认定为需求变更，变更费用按双方确认的实际工作量核定和支付；
在项目维护期内，运维服务要求如下：

第十二条  生效及其他
1、双方联系人

2、本合同自双方法定代表人或者授权签字人签章并加盖公章之日起生效。
3、除非本合同另有规定，任何一方希望变更或终止本协议的，须提前10日书面通知另一方，经双方协商一致，以书面形式进行变更或终止。合同终止前已经产生的权利和义务，不因合同的终止或相关方的延迟履行而灭失。
4、在本合同履行期间及履行完毕的任何时候，未经对方同意，任何一方不得以任何形式公开本合同及附件内容，以确保双方的商业机密。
5、因执行本合同而发生的争议，由当事人双方协商解决。协商不成，任何一方可依法向甲方所在地有管辖权的人民法院起诉。
5、本合同一式肆份。甲乙方各执贰份。附件为主合同的一部分，具有同等法律效力。

甲方（委托方）：武汉市汉阳市政建设集团有限公司
法定代表人： 王智高
委托代理人：徐志文
签订日期：

乙方（受托方）：武汉汇科智创科技有限公司
法定代表人：向仕华
委托代理人：柯贤富
签订日期：

附件1：项目开发费用清单

附件2：项目部署服务租赁清单

附录3：项目验收交付清单

附录4：技术设计要求清单
请检查发票金额是否正确，同时检测合同的其他地方是否和发票一致,比如公司名。"""},
    ],
)
print(completion.choices[0].message.content)

end_time = time.time()
response_time = end_time - start_time
print(f"Response Time: {response_time} seconds")

# # Streaming:
# print("----- streaming request -----")
# stream = client.chat.completions.create(
#     model="ep-20241220093718-lsmht",
#     messages = [
#         {"role": "system", "content": "你是豆包，是由字节跳动开发的 AI 人工智能助手"},
#         {"role": "user", "content": "常见的十字花科植物有哪些？"},
#     ],
#     stream=True
# )
# for chunk in stream:
#     if not chunk.choices:
#         continue
#     print(chunk.choices[0].delta.content, end="")
# print()