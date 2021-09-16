import discord
import asyncio
import datetime
import random
import os

client = discord.Client()

@client.event
async def on_ready():

    print(client.user.name)
    print('봇 부팅됨')
    game = discord.Game("StarCraft")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content == "저그봇아 스트롤가이봇에대해 어떻게 생각해?":
        await message.channel.send("아 그 병신같은 봇?")
    if message.content == "98년도 틀딱겜 기반으로한 봇이 지랄하네":
        await message.channel.send("병신같은 봇이 지랄하네 ㅋ")
    if message.content == "진짜 뒤질라고":
        await message.channel.send("어쩌라고 머리에 아무것도 없는 놈이 ㅋ 에휴 수듄 ㅋ")
    if message.content == "sd":
        await message.channel.send("```드론으로 변이 완료```")
    if message.content == "sz":
        await message.channel.send("```저글링으로 변이 완료```")
    if message.content == "so":
        await message.channel.send("```오버로드로 변이 완료```")
    if message.content == "sh":
        await message.channel.send("```히드라리스크로 변이 완료```")
    if message.content == "sm":
        await message.channel.send("```뮤탈리스크로 변이 완료```")
    if message.content == "ss":
        await message.channel.send("```스커지로 변이 완료```")
    if message.content == "sq":
        await message.channel.send("```퀸으로 변이 완료```")
    if message.content == "su":
        await message.channel.send("```울트라리스크로 변이 완료```")
    if message.content == "sf":
        await message.channel.send("```디파일러로 변이 완료```")
    if message.content == "g":
        await message.channel.send("```가디언으로 변이 완료```")
    if message.content == "u":
        await message.channel.send("```성큰콜로니로 변이 완료```")
    if message.content == "s":
        await message.channel.send("```스포어콜로니로 변이 완료```")
    if message.content == "bs":
        await message.channel.send("```스포닝풀로 변이 완료```")
    if message.content == "be":
        await message.channel.send("```익스트레터로 변이 완료```")
    if message.content == "bv":
        await message.channel.send("```에볼루션 쳄버로로 변이 완료```")
    if message.content == "bd":
        await message.channel.send("```히드라리스크 덴으로 변이 완료```")
    if message.content == "vs":
        await message.channel.send("```스파이어로 변이 완료```")
    if message.content == "vq":
        await message.channel.send("```퀸스네스트로 변이 완료```")
    if message.content == "vn":
        await message.channel.send("```나이더스 커널로 변이 완료```")
    if message.content == "vu":
        await message.channel.send("```울트라리스크 캐번으로 변이 완료```")
    if message.content == "vd":
        await message.channel.send("```디파일러 마운드로 변이 완료```")
    if message.content == "g":
        await message.channel.send("```그레이터스 스파이어로 변이 완료```")
    if message.content == "l":
        await message.channel.send("```레어로 변이 완료```")
    if message.content == "h":
        await message.channel.send("```하이브로 변이 완료```")
    if message.content == "저그 울트라리스크 대사":
        await message.channel.send("(rore)")
    if message.content == "저그 디바우러 대사":
        await message.channel.send("(rore)")
    if message.content == "스타 저글링 정보":
        embed = discord.Embed(title="저글링", description="저글링 Zergling/온통 모래로 덮인 행성 즈가시에 사는 작고 잔혹한 듄러너은 정찰과 돌격대 임무의 수행을 위해 저그 종족으로 흡수되었다. 저글링은 지능이나 육체적 능력은 야생 동물보다 그다지 나을 것이 없지만, 많은 수가 모이면 주요 저그 전사들의 지휘 하에 대규모 작전 전개가 가능하다. 저글링은 돌출부의 면도날처럼 날카로운 낫과 송곳니로 적을 갈가리 찢어버리는 것을 즐긴다. 저글링의 유전자는 복제하기가 매우 간단하여, 애벌레 하나가 저글링 두 마리로 변신할 수 있다.")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877831447627595780/882855282219307058/Z.png")
        embed.set_footer(text="역할 : 소형 돌격대 (Light Assault Warrior) / 출신 : 즈가시 듄러너 (Zz'gashi Dune-runners) / 주 무기발톱 : (Claws)")
        await message.channel.send(embed=embed)
    if message.content == "스타 드론 정보":
        embed = discord.Embed(title="드론", description="Drone, 드론/엘더스타인(Eldersthine)/행성의 야생 가쉬르 말벌은 원래 자원 수집을 담당하기 위해 저그에 편입되었다. 시간이 흐름에 따라 말벌은 애벌레의 능력을 전수받아 일벌레(Drone)로 진화하였다. 일벌레는 애벌레처럼 자신의 유전자 정보를 변경하여 초기 형태의 저그 건물로 변신할 수 있다.변신하려는 일벌레는 그에 필요한 영양분과 물질을 공급받으려면 반드시 점막 위에 있어야 한다. 애벌레와 마찬가지로 일벌레 역시 대군주(Overlord)의 지배를 받는다. 대군주는 일종의 텔레파시로 일벌레의 성장을 관찰한다. 일벌레는 치열한 전투가 벌어지는 도중에도 묵묵히 자신의 일에만 몰두할 정도로 그 성질이 단순하다.")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877831447627595780/882859176156602448/2Q.png")
        embed.set_footer(text="역할 : 군락 일꾼 (Hive Worker) / 출신 종 : 가쉬르 말벌 (Gashyrr Wasp) / 주 무기 : 가시뼈 (Spines)")
        await message.channel.send(embed=embed)
    if message.content == "스타 라바 정보":
        embed = discord.Embed(title="라바", description="Larva, 라바/벌레 모습을 한 저그의 원래 형태에 가장 가까운 유닛이 바로 이 애벌레이다. 젤나가의 반복적인 실험으로 애벌레의 크기와 힘은 크게 증가했고, 원래 위대한 창조주의 관심을 끌었던 두 가지 장점인 유전적으로 뛰어난 다변성과 사이오닉 에너지 감응력 또한 보존되고 있다.각각의 애벌레는 모든 저그 종의 유전 정보를 가질 수 있다. 생성된지 얼마 되지 않은 군락은 일꾼과 같은 가장 간단한 저그 계통의 유전 정보밖에는 가지고 있지 않다. 하지만 군락이 차츰 성장함에 따라 애벌레는 다양한 유전자 정보를 가질 수 있다. 초월체의 명령에 따라 애벌레는 고치 상태에 들어가 군락에서 요구하는 형태로 탈바꿈 한다.")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877831447627595780/882861965024825384/9k.png")
        embed.set_footer(text="역할 : 군락 생성 (Hive Spawn) / 출신 종 : 저그 (Original Zerg Strain) / 주 무기 : 없음")
        await message.channel.send(embed=embed)
    if message.content == "스타 오버로드 정보":
        embed = discord.Embed(title="오버로드", description="Overlord, 오버로드/준 지성체 가간티스 프록시매는 스스로 우주 여행을 할 수 있는 거대한 동물이었다. 저그는 가간티스 프록시매의 발달된 감각을 활용하여 전장에서 저그의 전사들을 지원하기 위해 이 생명체를 흡수했다. 가간티스 프록시매는 저그 종족에 아무런 저항도 없이 동화되었고, 정신체는 자신의 부대에 대한 확고한 지배를 유지하는데 그들을 활용했다. 대군주는 전투가 진행되는 동안 저그 족의 전사들에게 명령을 내리고 질서를 유지하며, 때로는 발달된 감각 기능을 이용하여 정찰기로서의 역할을 수행하기도 한다. 그들은 숨어 있는 적 유닛을 발견하는 선천적인 능력을 갖추고 있으며, 심지어는 은폐 장비나 시공간의 왜곡을 통해 숨어 있는 적도 발견할 수 있다.적에 대항하여 부대를 지휘하는 것 외에, 대군주는 강화된 껍질 내부의 빈 공간에 저그 전사들을 실어 수송하는 역할도 수행한다. 이러한 형태의 대군주는 오직 유전적으로 복낭 강화 능력을 갖춘 서식지나 군락에서만 생산할 수 있다.")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877831447627595780/882862838522195968/cd271001116adebd8c8e33d47deb3b3f58c38beaf75f6579ac19223c81523592bcef561b4a56ba566c20f9ee5791d0880ef5.png")
        embed.set_footer(text="역할 : 공중 지휘관 (Airborne Commander) / 중(重)형 수송선 (Heavy Transport (Advanced Strains)) / 출신 : 종족가간티스 프록시매 (Gargantis Proximae) / 주 : 무기없음, 다른 유닛들을 내부에 실을 수 있음 (None; may house other breeds)")
        await message.channel.send(embed=embed)
    if message.content == "스타 오버시어 정보":
        embed = discord.Embed(title="오버시어", description="Overseer 오버시어/감시 군주는 2차 대전쟁 때 발견된 유전적으로 변형된 대군주로서 극도로 민감한 망막이 달린 진화된 시각 기관을 갖추고 있다. 감시 군주의 눈은 반복적인 과정을 겪으며 계속해서 발전 주기마다 시각적인 진화를 이룩해 왔다.저그는 미세한 움직임과 진보된 은폐 기술을 간파하는 데 집착했으며, 감시 군주는 최근에 이뤄진 이러한 진화를 통해 지하에 잠복해 있거나 은폐하여 숨어 있는 모든 적 유닛을 찾아낼 수 있는 능력을 얻는 대신 아군 수송 능력을 잃어버리게 되었다.또한 감시 군주는 다양한 능력을 지니고 있다. 이 능력은 두 가지로 적의 구조물에 뿌려 일시적으로 기능을 마비시키는 오염 능력과 처음 눈에 마주친 적 개체와 똑같이 자신의 몸과 색깔을 바꾸며 적의 종족에 따라 다르게 변신하는 잠입용 생명체인 변신수를 생성하는 능력이다. 감시 군주의 이러한 능력들 중에서 가장 골치아픈 능력은 저그, 테란, 프로토스 각 종족을 모방할 수 있는 잠입용 생명체인 변신수를 낳거나 운반할 수 있다는 능력이 아닐까.")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877831447627595780/882863753828376606/207169464EB4AEF425.png")
        await message.channel.send(embed=embed)
    if message.content == "스타 울트라리스크 정보":
        embed = discord.Embed(title="울트라리스크", description="Ultralisk, 울트라리스크/원래의 조상인 온순한 브론톨리스와 전혀 닮은 바가 없어 보이는 울트라리스크는 저그의 지상 병력 중 가장 강력한 유닛이다. 저그의 주력 지상군인 이들은 어떤 종족의 장갑 차량보다도 강력하다. 이 거대한 괴물은 어떤 적에 대해서도 효과적인 공격 병기로 활용된다. 그들의 등에서 뻗어 나온 거대한 뼈처럼 생긴 날은 거의 파괴할 수 없을 정도로 단단하고, 어떤 물질이라도 가볍게 자를 수 있다. 이 괴물에 접근하는 가장 좋은 방법은 공중에서 공격을 가하는 것이다.")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877831447627595780/882885690596155423/Z.png")
        embed.set_footer(text="역할 : 대형 돌격대 (Heavy Assault Warrior) / 출신 종 : 브론톨리스 (Brontolith)[2] / 주 무기 : 카이저 칼날 (Kaiser Blades)")
        await message.channel.send(embed=embed)
    if message.content == "스타 스커지 정보":
        embed = discord.Embed(title="스커지", description="Scourge, 스커지/육중한 수호군주와 극명하게 대비되는 것이 바로 이 소형 갈귀이다. 눈이 없는 이 동물은 적 전함을 찾아내어 자살 공격을 가한다. 스커지의 몸에서 나오는 촉매제가 전함의 몸체와 충돌할 때 마치 플라즈마 폭탄처럼 폭발을 일으킨다. 많은 수의 스커지가 모이면 대규모의 전투기 편대나 심지어 전투순양함마저 격파할 수 있다. 스커지는 저글링과 마찬가지로 유전자 형태가 단순하기 때문에, 하나의 애벌레에서 두 마리가 태어난다.")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877831447627595780/882889701667799040/images.png")
        embed.set_footer(text="역할 : 고속 공격 유닛 (High Speed Attacker) / 출신 종 : 알 수 없음 / 주 무기 : 플라스마 변태 (Plasma Metamorphosis)")
        await message.channel.send(embed=embed)
    if message.content == "스타 뮤탈리스크 정보":
        embed = discord.Embed(title="뮤탈리스크", description="뮤탈리스크, Mutalisk/뮤탈리스크는 외진 디나레스 구역에 살던 만티스 스크리머에서 거의 변화하지 않았다. 대기와 우주 비행이 모두 가능한 뮤탈리스크는 저그 족의 공중 유닛들 중에서 핵심적인 역할을 담당한다. 뮤탈리스크는 적의 몸을 빠른 속도로 뚫고 나가는 공생체로 적을 공격한다.")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877831447627595780/882891546901508106/2Q.png")
        embed.set_footer(text="역할 : 중형 전투 유닛 (Medium Attack Flyer) / 출신 :  종만티스 스크리머 (Mantis Screamer, 비명 사마귀) / 주 무기 : 쐐기벌레 (Glave Wurm)")
        await message.channel.send(embed=embed)
    if message.content == "스타 히드라리스크 정보":
        embed = discord.Embed(title="히드라리스크", description="히드라리스크 Hydralisk/슬로시엔은 원래 평화로운 초식 동물이었다. 그러나 저그에 편입된 후 이 초식 동물은 저그 종족 중에서도 가장 사납고 악마같은 전사로 변신했다. 초월체는 송충이를 닮은 슬로시엔의 유전자를 조작하여, 이 불운한 동물을 히드라리스크라는 이름으로 알려진 악몽에서나 등장할 법한 살육자로 변화시켰다. 한때 온순한 동물이었던 히드라리스크는 이제 피와 폭력에 굶주린 동물로 변했다.기다란 뱀을 닮은 히드라리스크의 외피에는 수백 개의 가시뼈가 꽂혀있다. 히드라리스크는 공중이나 육상으로 접근하는 적을 향해 이 가시뼈를 발사할 수 있다.[1] 따라서 히드라리스크가 몰려있는 곳에는 매우 조심스럽게 접근해야 한다.")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877831447627595780/883140834088878160/image.png")
        embed.set_footer(text="역할 : 중형 돌격대 (Medium Assault Warrior) / 출신 : 종슬로시엔 (Slothien) / 주 무기 : 바늘 가시뼈 (Needle Spines)")
        await message.channel.send(embed=embed)
    if message.content == "스타 퀸 정보":
        embed = discord.Embed(title="퀸", description="여왕, Queen/저그 종족의 여왕은 이름과는 달리 애벌레를 낳지는 않는다. 하지만 여왕의 지위는 기생충을 닮은 여러 가지 동물을 낳을 수 있는 능력에서 얻어진 것이다. 여왕은 스스로 공격할 수 있는 능력이 없고 연약한 갑옷 때문에 적의 공격에 대단히 취약하므로, 주로 군락의 중앙에 거주하며 다른 저그의 성장을 지켜보곤 한다.")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877831447627595780/882895329207390208/xdlkLSYW9Jvkp47iL2EwHYq5-aTqiw5TbIOcg7JFOEP8fkRvUvXWJLA61jGAPvylpKryv2bgXKITwaJ8f8YvR6ZAd0nnZYx58Z_Z.png")
        embed.set_footer(text="역할 : 군락 감시자 (Hive Warden) / 출신 종족 : 아라크니스 종족 사육자 (Arachnis Brood-keeper) / 주 무기 : 없음(비무장)")
        await message.channel.send(embed=embed)
    if message.content == "스타 디파일러 정보":
        embed = discord.Embed(title="디파일러", description="Defiler, 디파일러/파멸충은 저그의 광적이고 가학적인 본성을 잘 보여주는 표본이라고 할 수 있다. 애벌레와 마찬가지로 파멸충은 모든 저그 종족의 유전자를 보유하고 있다. 그러나 파멸충은 이 유전자 정보로 저그 종족을 생산하는 것이 아니라, 반대로 저그 족에게 치명적인 효과를 나타내는 악성 독소를 생산해 낸다. 파멸충은 또한 부식성 독을 뱉어서 자신을 방어할 수 있지만, 가능한 한 직접적인 전투는 피한다.")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877831447627595780/883210583606968380/2d4c3da4f2a811c9fc09c3667cb0af1c35704217e43672c5c85b3b16e1aca0670f916e680b7a38ef19334b12efb96cb4a036.png")
        embed.set_footer(text="역할 : 바이러스성 돌격대 (Viral Shock Trooper) / 출신 종족 : 알 수 없음 / 주 무기 : 없음 ")
        await message.channel.send(embed=embed)
    if message.content == "스타 럴커 정보":
        embed = discord.Embed(title="럴커", description="가시지옥 Lurker/저그 종족에 새로이 추가된 잔인한 전사 가시지옥은 저그의 군락과 외곽 기지의 방어용 유닛으로 이용된다. 가시지옥은 히드라리스크가 변태한 모습으로 고밀도의 가시 뭉치를 적에게 발사하는 공격 형태를 지녔지만, 잠복 상태가 아니면 이러한 지하 공격을 할 수 없다. 이 가시의 사정거리 안에 들어온 지상의 적은, 가시지옥에게 걸림과 동시에 몸체가 꿰뚫리고 만다. 이들의 가시는 피부나 금속뿐만 아니라 강화 처리된 장갑판 조차도 뚫을 수 있다. 가시지옥의 유일한 약점은 지상에 나와 있을 경우 방어력이 전혀 없다는 점이다.")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877831447627595780/887534756802224188/8fc74440cd2595bda043f02f4362f0c67d9f0032bd78d7fd79f03c5308e20306399dcf61e3a5d7ad978b41a18d22ef817c74.png")
        embed.set_footer(text="역할 : 중형 방어 부대 (Heavy Defense Warrior) / 출신종족 : 히드라리스크 / 주 무기: 지하 가시뼈 (Subterranean Spines)")
        await message.channel.send(embed=embed)
    if message.content == "스타 가디언 정보":
        embed = discord.Embed(title="가디언", description="Guardian, 가디언/뮤탈리스크는 한편 또 다른 형태로 변신할 수 있다. 이 형태는 비명 사마귀가 새끼를 낳을 때 취하는 모습으로 알려져 있다. 저그의 수호군주는 더욱 견고한 장갑을 갖추고, 뮤탈리스크의 공격보다 훨씬 원거리의 적을 공격할 수 있는 산 덩어리를 발사한다. 수호군주는 지상 유닛만 공격할 수 있으며, 공중 공격에 대응할 수 있는 무기는 갖추고 있지 않다.")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877831447627595780/887546419165143060/7964158032c96f26a65f58abe79d7714c4e365c2ba4cd41870ebfb6b7c09674a1fba6fead7a7991ef38284e189e1d81f7f1f.png")
        embed.set_footer(text="역할 : 공성 폭격기 (Siege Bomber) / 출신 종족 : 뮤탈리스크 / 주 무기 : 산성 포자 (Acid Spores)")
        await message.channel.send(embed=embed)
    if message.content == "스타 디바우러 정보":
        embed = discord.Embed(title="디바우러", description="Devourer, 디바우러/뮤탈리스크로부터 태어나는 포식귀는 저그의 '군단'에 새로 추가된 강력한 유닛이다. 이 거대한 비행체는 적 공중 유닛에 강력한 산성 물질을 내뿜어 적을 부식시킴과 동시에 큰 피해를 입힌다. 포식귀의 독액은 테란이나 프로토스 주력함의 강화 장갑판을 포함하여 어떠한 물질도 녹여 버리는 독소로 구성되어 있다. 포식귀가 발사한 산은 충돌과 동시에 사방으로 튀어 주위의 유닛에게도 피해를 준다.")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877831447627595780/887544272050614283/2Q.png")
        embed.set_footer(text="역할 : 중형 비행 돌격대 (Heavy Assault Flyer) / 출신 종 : 뮤탈리스크 / 주 무기 : 부식성 산 (Corrosive Acid)")
        await message.channel.send(embed=embed)
    if message.content == "스타 저그 정보":
        embed = discord.Embed(title="저그", description="저그는 초월체에 의해 군단에 흡수된 몇 가지 종류의 동물들로 이루어져 있다. 이들 생명체, 혹은 종은 각자의 효율적인 살인 병기 역할에 맞게 선택적으로 진화되어 궁극적인 힘을 얻으려는 저그의 목적에 봉사한다. 저그는 우리가 흔히 아는 과학 기술을 사용하지는 않지만, 고도로 진화한 무기와 갑피는 어떤 종족이 개발한 최첨단 장비와도 견줄 만하다. 이러한 생체 진화는 초월체에 대한 절대적인 충성심과 함께 저그를 우주에서 가장 두려운 존재 중 하나로 만들었다.저그의 생명 주기 (Zerg Life Cycle) : 저그는 다른 종족들처럼 군대를 조직하거나 훈련하지 않는다. 대신 중앙 집중식 부화장(Hatchery)이 애벌레(Larva)를 낳고, 이 애벌레들은 변태를 일으켜 다양한 저그 종족으로 자라난다. 이러한 생산 시스템은 모든 것이 중앙 집중식으로 이루어지는 저그의 장점이자 단점이기도 하다. 부화장은 어떤 수단을 동원해서라도 보호해야 하며, 애벌레의 생산량을 늘리려면 새로운 부화장을 가능한 한 많이 만들 필요가 있다.점막 (The Creep) : 저그의 구조물은 사실상 거대한 생체 기관이며, 저그 종족의 기지 전체는 하나의 생명체이다. 저그는 필요한 양분과 하부 구조를 제공하기 위하여 생체 물질로 이루어진 살아있는 깔개, 점막(Creep)을 식민지가 건설된 건물의 주위에 깐다. 부화장과 점막 군체(Creep Colony)가 생산해 내는 점막은 양분이 있는 땅의 표면이라면 어디에서든 아주 빠른 속도로 퍼져 나간다. 부화장은 점막이 없이도 건설할 수 있는 유일한 저그 건물이다. 이는 부화장이 성장에 필요한 에너지를 스스로 공급할 수 있도록 유전적으로 설계된 유일한 건물이기 때문이다. 점막 자체는 매우 튼튼하며, 거의 순간적으로 재생할 수 있다. 부화장이나 점막 군체가 파괴되지 않는 한 점막은 쉼없이 성장을 계속한다.재생 (Regeneration) : 저그 종족의 가장 큰 장점은 아마도 생체 구조상 자신을 스스로 치료하고 회복할 수 있다는 능력을 지니고 있다는 것이다. 저그 식민지의 모든 생명과 구조물을 완전히 파괴하기 전까지는 누구도 안심할 수 없다. 죽음 직전까지 도달한 저그라 할지라도 결국은 원래의 생명력을 되찾을 것이기 때문이다. 지배력 (Control) : 저그의 초월체는 지속적으로 자신의 부하들과 사이오닉 유대 관계를 유지한다. 하지만 각각의 개체에 명령을 내릴 때 초월체는 대군주(Overlord)를 통해 명령을 전달해야 한다. 저그 식민지는 모든 대군주의 지배력을 합한 것 이상으로는 성장할 수 없다. 지배력의 현재 상태는 항상 주 화면의 오른쪽 위에 표시된다. 대군주를 각각 선택해도 현재 사용 중인 지배력과 제공되는 지배력의 정도가 표시된다.")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877831447627595780/882897356155129866/wr.jpg")
        await message.channel.send(embed=embed)
    if message.content == "저그봇 명령어":
        await message.channel.send("```sd, sz, so, ss, sm, sh, su, sf, sq, u, s, bs, be, bv, vs, vq, vn, vu, vd, g, l, h, 스타 (유닛, 건물 띄워쓰기 x) 저그 (유닛,건물 정보 ex :저그건물, 저그유닛) 이름(띄워쓰기x)```")
    if message.content == "스타 정보 출처":
        await message.channel.send("```https://namu.wiki/w/%EC%A0%80%EA%B7%B8/%EA%B2%8C%EC%9E%84%20%EB%82%B4%20%ED%8A%B9%EC%A7%95#s-3.5```")
    if message.content == "저그 유닛정보 라바":
        embed = discord.Embed(title="라바", description="체력 : 25 / 공격무기없음 / 방어력 : 10 / 미네랄 : 0 / 가스 : 0 / 인구 : 0")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877831447627595780/882861965024825384/9k.png")
        await message.channel.send(embed=embed)
    if message.content == "저그 유닛정보 드론":
        embed = discord.Embed(title="드론", description="체력 : 40 / 공격력 : 5 / 방어력 : 0 / 미네랄 : 50 / 가스 : 0 / 생산시간 : 12.5초 / 인구 : 1")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877831447627595780/882859176156602448/2Q.png")
        await message.channel.send(embed=embed)
    if message.content == "저그 유닛정보 저글링":
        embed = discord.Embed(title="저글링", description="체력 : 35 / 공격력 : 5 / 방어력 : 0 / 미네랄 : 50 / 가스 : 0 / 생산시간 : 17.5초")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877831447627595780/882855282219307058/Z.png")
        await message.channel.send(embed=embed)
    if message.content == "저그 유닛정보 오버로드":
        embed = discord.Embed(title="오버로드", description="체력 : 200 / 공격무기없음 / 방어력 : 0 / 미네랄 : 100 / 가스 : 0 / 생산시간 : 25초 / 인구 : +8")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877831447627595780/882862838522195968/cd271001116adebd8c8e33d47deb3b3f58c38beaf75f6579ac19223c81523592bcef561b4a56ba566c20f9ee5791d0880ef5.png")
        await message.channel.send(embed=embed)
    if message.content == "저그 유닛정보 히드라리스크":
        embed = discord.Embed(title="히드라리스크", description="체력 : 80 / 공격력 : 10 / 방어력 : 0 / 미네랄 : 75 / 가스 : 25 / 생산시간 : 17.5초 / 인구 : 1")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877831447627595780/883140834088878160/image.png")
        await message.channel.send(embed=embed)
    if message.content == "저그 유닛정보 럴커":
        embed = discord.Embed(title="럴커", description="체력 : 125 / 공격력 : 20 / 방어력 : 1 / 미네랄 : 50 / 가스 : 100 / 생산시간 : 25초 / 인구 : 2(히드라리스크 상태에서 +1)")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877831447627595780/887534756802224188/8fc74440cd2595bda043f02f4362f0c67d9f0032bd78d7fd79f03c5308e20306399dcf61e3a5d7ad978b41a18d22ef817c74.png")
        await message.channel.send(embed=embed)
    if message.content == "저그 유닛정보 뮤탈리스크":
        embed = discord.Embed(title="뮤탈리스크", description="체력 : 120 / 공격력 : 9 / 방어력 : 0 / 미네랄 : 100 / 가스 : 100 / 생산시간 : 25초 / 인구 : 2")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877831447627595780/882891546901508106/2Q.png")
        await message.channel.send(embed=embed)
    if message.content == "저그 유닛정보 스커지":
        embed = discord.Embed(title="스커지", description="체력 : 25 / 공격력 : 110 / 방어력 : 0 / 미네랄 : 25 / 가스 : 75 / 생산시간 : 18.75초 / 인구 : 0.5 / 시야 : 5 / 장갑 : 소형")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877831447627595780/882889701667799040/images.png")
        await message.channel.send(embed=embed)
    if message.content == "저그 유닛정보 퀸":
        embed = discord.Embed(title="퀸", description="체력 : 120 / 공격무기없음 / 방어력 : 0 / 미네랄 : 100 / 가스 : 100 / 생산시간 : 31.25초 / 인구 : 2 / 시야 : 10 / 장갑 : 중형 / 능력 : 패러사이트, 스폰 브루들링, 인스네어, 인페스테이션")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877831447627595780/882895329207390208/xdlkLSYW9Jvkp47iL2EwHYq5-aTqiw5TbIOcg7JFOEP8fkRvUvXWJLA61jGAPvylpKryv2bgXKITwaJ8f8YvR6ZAd0nnZYx58Z_Z.png")
        await message.channel.send(embed=embed)
    if message.content == "저그 유닛정보 울트라리스크":
        embed = discord.Embed(title="울트라리스크", description="체력 : 400 / 공격력 : 20 / 방어력 : 1 / 미네랄 : 200 / 가스 : 200 / 생산시간 : 37.5초 / 인구 : 4 / 시야 : 7 / 장갑 : 대형")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877831447627595780/882885690596155423/Z.png")
        await message.channel.send(embed=embed)
    if message.content == "저그 유닛정보 디파일러":
        embed = discord.Embed(title="디파일러", description="체력 : 80 / 공격무기없음 / 방어력 : 1 / 미네랄 : 50 / 가스 : 150 / 생산시간 : 31.25초 / 인구 : 2 / 시야 : 10 / 장갑 : 중형 / 능력 : 다크스웜, 플레이그,버로우, 컨슘")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877831447627595780/883210583606968380/2d4c3da4f2a811c9fc09c3667cb0af1c35704217e43672c5c85b3b16e1aca0670f916e680b7a38ef19334b12efb96cb4a036.png")
        await message.channel.send(embed=embed)
    if message.content == "저그 유닛정보 가디언":
        embed = discord.Embed(title="가디언", description="체력 : 150 / 공격력 : 20 / 방어력 : 2 / 미네랄 : 50 / 가스 : 100 / 생산시간 : 25초 / 인구 : 2(뮤탈리스크 상태에서 0) / 시야 : 11 / 장갑 : 대형")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877831447627595780/887546419165143060/7964158032c96f26a65f58abe79d7714c4e365c2ba4cd41870ebfb6b7c09674a1fba6fead7a7991ef38284e189e1d81f7f1f.png")
        await message.channel.send(embed=embed)
    if message.content == "저그 유닛정보 디바우러":
        embed = discord.Embed(title="디바우러", description="체력 : 250 / 공격력 : 25 / 방어력 : 2 / 미네랄 : 150 / 가스 : 50 / 생산시간 : 25초 / 인구 : 2(뮤탈리스크 상태에서 0)")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877831447627595780/887544272050614283/2Q.png")
        await message.channel.send(embed=embed)
    if message.content == "저그 건물정보 해처리":
        embed = discord.Embed(tilte="해처리", description="체력 : 1250 / 방어력 : 1 / 미네랄 : 300 / 가스 : 0 / 생산시간 : 75초 / 시야 : 9 / 능력 : 라바생성, 버로우 업그레이드, 레어 변태 / 인구 : +1")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877831447627595780/887700777437626458/img.png")
        await message.channel.send(embed=embed)
    if message.content == "저그 건물정보 레어":
        embed = discord.Embed(tilte="레어", description="체력 : 1800 / 방어력 : 1 / 미네랄 : 150 / 가스 : 100 / 생산시간 : 62.5 / 시야 : 10 / 능력 : 오버로드 수송 업그레이드, 오버로드 시야 업그레이드, 오버로드 속도 업그레이드, 하이브변태 / 인구 : +1")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877831447627595780/887701624020168834/2Q.png")
        await message.channel.send(embed=embed)
    if message.content == "저그 건물정보 하이브":
        embed = discord.Embed(tilte="하이브", description="체력 : 2500 / 방어력 : 1 / 미네랄 : 200 / 가스 : 150 / 생산시간 : 75초 / 시야 : 11 / 능력 : 오버로드 수송 업그레이드, 오버로드 시야 업그레이드, 오버로드 속도 업그레이드, 하이브변태 / 인구 : +1")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877831447627595780/887702134848643072/C7CFC0CCBAEA.png")
        await message.channel.send(embed=embed)
    if message.content == "저그 건물정보 크립콜로니":
        embed = discord.Embed(tilte="크립콜로니", description="체력 : 400 / 방어력: 0 / 미네랄 : 75 / 가스 : 0 / 생산시간 : 12.5 / 시야 : 10 / 능력 : 성큰 콜로니 변태, 스포어 콜로니 변태")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877831447627595780/887702683073519636/img.png")
        await message.channel.send(embed=embed)
    if message.content == "저그 건물정보 성큰콜로니":
        embed = discord.Embed(tilte="성큰콜로니", description="체력 : 300 / 공격력 : 40 / 방어력 : 2 / 미네랄 : 50 / 가스 : 0 / 생산시간 : 12.5초 / 시야 : 10 / 능력 : 지상공격")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877831447627595780/887703482742755328/9k.png")
        await message.channel.send(embed=embed)
    if message.content == "저그 건물정보 스포어콜로니":
        embed = discord.Embed(tilte="스포어콜로니", description="체력 : 400 / 공격력 : 15 / 방어력 : 0 / 미네랄 : 50 / 가스 : 0 / 생산시간 : 12.5초 / 시야 : 10 / 능력 : 공중 공격, 디텍터")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877831447627595780/887704292868386866/9k.png")
        await message.channel.send(embed=embed)
    if message.content == "저그 건물정보 익스트랙터":
        embed = discord.Embed(tilte="익스트랙터", description="체력 : 750 / 방어력 : 1 / 미네랄 : 50 / 가스 : 0 / 생산시간 : 25초 / 시야 : 7")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877831447627595780/887704844289314847/BDBAC5B82.png")
        await message.channel.send(embed=embed)
    if message.content == "저그 건물정보 스포닝풀":
        embed = discord.Embed(tilte="스포닝풀", description="체력 : 750 / 방어력 : 1 / 미네랄 : 200 / 가스 : 0 / 생산시간 : 50초 / 시야 : 8 / 능력 : 저글링 속도 업그레이드")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877831447627595780/887705366538899587/img.png")
        await message.channel.send(embed=embed)
    if message.content == "저그 건물정보 에볼루션챔버":
        embed = discord.Embed(tilte="에볼루션챔버", description="체력 : 750 / 방어력 : 1 / 미네랄 : 75 / 가스 : 0 / 생산시간 : 25초 / 시야 : 8 / 능력 : 저글링, 울트라리스크, 브루들링 공격력 업그레이드")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877831447627595780/887706395783331870/9k.png")
        await message.channel.send(embed=embed)
    if message.content == "저그 건물정보 히드라리스크덴":
        embed = discord.Embed(tilte="히드라리스크덴", description="체력 : 850 / 방어력 : 1 / 미네랄 : 100 / 가스 : 50 / 생산시간 : 25초 / 시야 : 8 / 능력 : 히드라리스크 속도 업그레이드")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877831447627595780/887707205573427300/10850cf3a1669b801b56a9bd460794b9b9dcdf977c67ee20d9dd16a9ae933c6d.png")
        await message.channel.send(embed=embed)
    if message.content == "저그 건물정보 스파이어":
        embed = discord.Embed(tilte="스파이어", description="체력 : 600 / 방어력 : 1 / 미네랄 : 200 / 가스 : 150 / 생산시간 : 75초 / 시야 : 8 / 능력 : 뮤탈리스크, 가디언, 디바우러 공격력 업그레이드")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877831447627595780/887707922329653258/BDBAC5B85.png")
        await message.channel.send(embed=embed)
    if message.content == "저그 건물정보 그레이터스파이어":
        embed = discord.Embed(tilte="그레이터스파이어", description="체력 : 1000 / 방어력 : 1 / 미네랄 : 100 / 가스 : 150 / 생산시간 :75초 / 시야 : 8 / 능력 : 뮤탈리스크, 가디언, 디바우러 공격력 업그레이드")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877831447627595780/887883847700738088/9k.png")
        await message.channel.send(embed=embed)
    if message.content == "저그 건물정보 퀸즈네스트":
        embed = discord.Embed(tilte="퀸즈네스트", description="체력 : 850 / 방어력 : 1 / 미네랄 : 150 / 가스 : 100 / 생산기간 :37.5초 / 시야 : 8 / 능력 : 스폰 브루들링 업그레이드")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877831447627595780/887884335217254520/2Q.png")
        await message.channel.send(embed=embed)
    if message.content == "저그 건물정보 나이더스커널":
        embed = discord.Embed(tilte="나이더스커널", description="체력 : 250 / 방어력 : 1 / 미네랄 : 150 / 가스 : 0 / 생산시간 : 25초 / 시야 : 8 / 능력 : 나이더스커널 연결")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877831447627595780/887884798150987876/img.png")
        await message.channel.send(embed=embed)
    if message.content == "저그 건물정보 울트라리스크캐번":
        embed = discord.Embed(tilte="울트라리스크캐번", description="체력 : 600 / 방어력 : 1 / 미네랄 : 150 / 가스 : 200 / 생산시간 : 50초 / 시야 : 8 / 능력 : 울트라리스크 생산 및 속도 업그레이드, 방어력 업그레이드")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877831447627595780/887885920563511306/606246d89424a07483b3fec21112bf78d74bfa29c52a3f56d3bf6cc2fff37016.png")
        await message.channel.send(embed=embed)
    if message.content == "저그 건물정보 디파일러마운드":
        embed = discord.Embed(title="디파일러마운드", description="체력 : 850 / 방어력 : 1 / 미네랄 : 100 / 가스 : 100 / 생산시간 : 37.5초 / 시야 : 8 / 능력 : 디파일러 생산 및 업그레이드 플레이그 업그레이드, 컨슘업그레이드, 디파일러마나 +50 업그레이드")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877831447627595780/887887349978132571/SE-c0bd4e38-86eb-453c-b6bb-29dd54173fd7.png")
        await message.channel.send(embed=embed)
    if message.content == "스타 스포닝풀 정보 ":
        embed = discord.Embed(title="스포닝풀", discription="고대의 모습을 그대로 유지한 산란못에는 저그 용사들 중 가장 잘 알려진 용맹한 저글링의 유전자가 보관되어 있다. 산란못은 애벌레가 저글링으로 변신하는 데 필요한 유전자 정보를 제공해 준다.")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877831447627595780/887705366538899587/img.png")
        await message.channel.send(embed=embed)
    if message.content == "스타 하이브 정보 ":
        embed = discord.Embed(title="하이브", discription="부화장이 가장 진화한 형태가 바로 이 군락이다. 고밀도 외골격으로 보호되고 초월체의 모든 지식에 자유자재로 접할 수 있는 군락은 가장 복잡한 건물과 종족을 생산해 낼 수 있다.")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877831447627595780/887702134848643072/C7CFC0CCBAEA.png")
        await message.channel.send(embed=embed)
    if message.content == "스타 성큰콜로니 정보 ":
        embed = discord.Embed(title="성큰콜로니", discription="대공 유닛을 상대로 뛰어난 대공 방어 능력을 보여 주는 포자 군체와는 달리, 지하 군체는 지상 공격으로부터 군락을 보호한다. 점막 깊은 곳까지 뿌리를 내리는 지하 군체는 여러 개의 촉수를 사용하여 접근하는 적에게 무시무시한 공격을 가한다.")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877831447627595780/887703482742755328/9k.png")
        await message.channel.send(embed=embed)
    if message.content == "스타 스포어콜로니 정보 ":
        embed = discord.Embed(title="스포어콜로니", discription="포자 군체로 변신한 점막 군체는 대군주와 유사한 감각 기관을 갖게 된다. 이 기관 덕분에 포자 군체는 은폐하거나 숨은 적 유닛을 판별할 능력을 지닌다. 또한 포자 군체는 부식성이 있는 변형물을 생산하여 접근하는 적의 공중 유닛을 향하여 발사한다.")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877831447627595780/887704292868386866/9k.png")
        await message.channel.send(embed=embed)
    if message.content == "스타 레어 정보 ":
        embed = discord.Embed(title="레어", discription="번식지로 진화, 혹은 '성숙'한 부화장은 더 견고할 뿐만 아니라 초월체의 유전적 지식을 더 많이 활용할 수 있다. 따라서 번식지는 저그 일꾼이 더욱 복잡한 건물로 변신할 수 있는 터전이 된다. 새로 건설된 건물은 역으로 유전 신호를 전달하여 애벌레가 새로운 종으로 변신할 수 있게 해 준다.")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877831447627595780/887701624020168834/2Q.png")
        await message.channel.send(embed=embed)
    if message.content == "스타 익스트렉터 정보 ":
        embed = discord.Embed(title="익스트렉터", discription="저그는 높은 에너지를 지닌 베스핀 가스를 이용하여 자신들의 활발한 신진대사를 유지하고 애벌레의 성장을 촉진한다. 추출장은 베스핀 간헐천 위에 설치하는 거대한 생체 기관이다. 추출장은 베스핀 가스를 작은 주머니에 포장하여 저그 일꾼이 가까운 부화장으로 쉽게 옮길 수 있게 한다. 추출장은 베스핀 가스를 먹고 살기 때문에 점막 위가 아니라도 지을 수 있다.")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877831447627595780/887704844289314847/BDBAC5B82.png")
        await message.channel.send(embed=embed)
    if message.content == "스타 에볼루션챔버 정보 ":
        embed = discord.Embed(title="에볼루션챔버", discription="초월체는 스스로 만족하는 순간 멸망의 길을 걷게 될 것이라는 사실을 잘 알고 있다. 따라서 초월체는 자신의 자손들을 끝없이 진화시켜 더욱 효과적인 살육 병기로 변모시키려 한다. 진화실은 초월체가 다양한 유전자 정보를 실험하여 저그 개체의 육체적 능력을 향상시키는 장소이다.")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877831447627595780/887706395783331870/9k.png")
        await message.channel.send(embed=embed)
    if message.content == "스타 히드라리스크덴 정보 ":
        embed = discord.Embed(title="히드라리스크덴", discription="히드라리스크 굴은 한때 온순한 종족이었던 슬로시엔의 둥우리와는 거의 공통점이 없다. 끈적한 점액질로 덮인 이 고약한 장소에 히드라리스크 전사들을 생산하기 위해 필요한 유전자 정보가 보관되어 있다.")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877831447627595780/887707205573427300/10850cf3a1669b801b56a9bd460794b9b9dcdf977c67ee20d9dd16a9ae933c6d.png")
        await message.channel.send(embed=embed)
    if message.content == "스타 스파이어 정보 ":
        embed = discord.Embed(title="스파이어", discription="뮤탈리스크로 변신한 만티스 스크리머는 한때 아무도 살지 않는 세계의 고지대에 둥지를 짓곤 했었다. 둥지탑은 만티스의 공중 둥지와 모습은 비슷하지만 점막에서 양분을 공급받아야만 생존할 수 있도록 변형되었다.")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877831447627595780/887707922329653258/BDBAC5B85.png")
        await message.channel.send(embed=embed)
    if message.content == "스타 퀸즈네스트 정보 ":
        embed = discord.Embed(title="", discription="온통 썩어 곪은 듯한 여왕의 둥지는 점막에서 영양을 공급받으며 여왕에게 다양한 능력을 부여한다. 둥지 주변에 난 구멍에는 여왕에게 영양분을 공급받는 여러 기생충의 군체가 서식한다. 여왕의 '자손'들은 반대로 자신을 희생하여 초월체의 명령을 따른다.")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877831447627595780/887884335217254520/2Q.png")
        await message.channel.send(embed=embed)
    if message.content == "스타 나이더스커널 정보 ":
        embed = discord.Embed(title="나이더스커널", discription="땅굴관의 정확한 근원은 알려져 있지 않으며, 그 동작 방식 역시 수수께끼로 남아 있다. 첫 번째 관의 입구가 생성된 후 적절한 장소가 발견되면 두 번째 입구가 생성된다. 그 후 관은 저그 지상 유닛들이 한쪽 입구에서 다른 쪽 입구로 중간 지형에 구애받지 않고 신속한 속도로 이동할 수 있는 통로 역할을 수행한다. 땅굴관은 여러 개의 부화장이 마치 하나의 통합된 둥지처럼 작용할 수 있게 해 주며, 저그 전사들은 한 전투 지역에서 다른 전투 지역으로 빠르고 효과적으로 이동할 수 있다.")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877831447627595780/887884798150987876/img.png")
        await message.channel.send(embed=embed)
    if message.content == "스타 울트라리스크캐번 정보 ":
        embed = discord.Embed(title="울트라리스크캐번", discription="단단한 울트라리스크 동굴 깊숙한 곳에는 높은 방사성을 띤 물질과 유독성 물질들이 가득하다. 동굴 속의 가혹한 환경은 역으로 울트라리스크에게 강력한 힘을 선사해 주었다. 울트라리스크의 유전자는 끝없는 실험과 시험을 거쳤으며, 오직 가장 우수한 유전자를 가진 애벌레만이 선택되어 울트라리스크로 변신한다.")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877831447627595780/887885920563511306/606246d89424a07483b3fec21112bf78d74bfa29c52a3f56d3bf6cc2fff37016.png")
        await message.channel.send(embed=embed)
    if message.content == "스타 디파일러마운드 정보 ":
        embed = discord.Embed(title="디파일러마운드", discription="파멸충 언덕 주변에는 파멸충의 몸에서 뿜어져 나오는 극히 유독한 물질에 오염된 광물질이 여기저기에 흩어져 있다. 그 바닥에는 유독성 액체가 역겨운 냄새를 풍기며 끓고 있으며, 이 유독성 액체 속에서 파멸충이 무기로 사용하는 다양한 독이 발생된다")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877831447627595780/887887349978132571/SE-c0bd4e38-86eb-453c-b6bb-29dd54173fd7.png")
        await message.channel.send(embed=embed)
    if message.content == "스타 그레이터스파이어 정보":
        embed = discord.Embed(title="그레이터스파이어", discription="더욱 두꺼운 장갑을 갖춘 거대 둥지탑은 가장 강력한 공중 유닛의 유전 정보를 제공하고 기존 유닛의 능력을 더욱 강화한다. 이 건물은 뮤탈리스크가 수호군주로 변신할 수 있게 해 주고, 수호군주가 된 뮤탈리스크는 속도와 공중 공격력을 희생하는 대신 강력한 지상 공격력을 얻는다.")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877831447627595780/887883847700738088/9k.png")
        await message.channel.send(embed=embed)
    if message.content == "저그 드론 대사":
        ran = random.randint(0,6)
        if ran == 0:
            d = "Proceed"
        if ran == 1:
            d = "I await"
        if ran == 2:
            d = "Make your choice"
        if ran == 3:
            d = "Sustaining the conquest"
        if ran == 4:
            d = "Yes, Leader"
        if ran == 5:
            d = "The time is now"
        if ran == 6:
            d = "It will be done"
        await message.channel.send(d)
    if message.content == "저그 저글링 대사":
        ran = random.randint(0,6)
        if ran == 0:
            d = "My talons are yours"
        if ran == 1:
            d = "I seek Essence"
        if ran == 2:
            d = "Lead us to power"
        if ran == 3:
            d = "Yes, Leader?"
        if ran == 4:
            d = "Weak will perish"
        if ran == 5:
            d = "My hunt continues"
        if ran == 6:
            d = "As you desire"
        await message.channel.send(d)
    if message.content == "저그 히드라리스크 대사":
        ran = random.randint(0,7)
        if ran == 0:
            d = "The fittest shall survive"
        if ran == 1:
            d = "We are ready to kill"
        if ran == 2:
            d = "I listen"
        if ran == 3:
            d = "What are your commands?"
        if ran == 4:
            d = "Our prey nears"
        if ran == 5:
            d = "Without question"
        if ran == 6:
            d = "Yes, my leader"
        if ran == 7:
            d = "Agreed"
        await message.channel.send(d)
    if message.content == "저그 럴커 대사":
        ran = random.randint(0,10)
        if ran == 0:
            d = "Death to the surfaced dwellers!"
        if ran == 1:
            d = "Where shall i strike?"
        if ran == 2:
            d = "Direct my wrath!"
        if ran == 3:
            d = "Yes, surfacee dweller?"
        if ran == 4:
            d = "Is it safe?"
        if ran == 5:
            d = "As you wish"
        if ran == 6:
            d = "I will honor our pact"
        if ran == 7:
            d = "I will strike!"
        if ran == 8:
            d = "Why should i?"
        if ran == 9:
            d = "I think i just slithered in something"
        if ran == 10:
            d = "I cant't smell... I bit my tongue?"
        await message.channel.send(d)
    if message.content == "저그 디파일러 대사":
        ran = random.randint(0,7)
        if ran == 0:
            d = "I live"
        if ran == 1:
            d = "I will collect"
        if ran == 2:
            d = "So much Essence"
        if ran == 3:
            d = "I listen"
        if ran == 4:
            d = "All things change"
        if ran == 5:
            d = "Essence flows, I follow"
        if ran == 6:
            d = "I go"
        if ran == 7:
            d = "Yes, Pack Leader"
        await message.channel.send(d)
    if message.content == "저그 뮤탈리스크 대사":
        ran = random.randint(0,6)
        if ran == 0:
            d = "We rule the skies"
        if ran == 1:
            d = "Our enemies will burn"
        if ran == 2:
            d = "Vanguard of the True Zerg!"
        if ran == 3:
            d = "Command me, Pack Leader"
        if ran == 4:
            d = "I claim their Essence"
        if ran == 5:
            d = "Seek and consume"
        if ran == 6:
            d = "The Pack obeys you"
        await message.channel.send(d)
    if message.content == "저그 가디언 대사":
        ran = random.randint(0,8)
        if ran == 0:
            d = "Vanquish the weak!"
        if ran == 1:
            d = "Don't waste my time"
        if ran == 2:
            d = "You call on me?"
        if ran == 3:
            d = "How will this benefit me??"
        if ran == 4:
            d = "I await your counsel"
        if ran == 5:
            d = "By any means neccessary"
        if ran == 6:
            d = "Right"
        if ran == 7:
            d = "I'll  do what i must"
        await message.channel.send(d)
        if ran == 8:
            d = "I'll  do what i must"
    if message.content == "저그 퀸 대사":
        ran = random.randint(0,6)
        if ran == 0:
            d = "The time to awaken has come"
        if ran == 1:
            d = "Come closer mores"
        if ran == 2:
            d = "We out feel with great hunger"
        if ran == 3:
            d = "This land shall be defiled"
        if ran == 4:
            d = "We shall feed"
        if ran == 5:
            d = "By hunger"
        if ran == 6:
            d = "Now!"
        await message.channel.send(d)
        
    if message.content.startswith("저그봇 현재시간"):
        a = datetime.datetime.today().year
        b = datetime.datetime.today().month
        c = datetime.datetime.today().day
        d = datetime.datetime.today().hour
        e = datetime.datetime.today().minute
        f = datetime.datetime.today().second
        await message.channel.send(str(a) + "년" + str(b) + "월" + str(c) + "일" + str(d) + "시" + str(e) + "분" + str(f) + "초")

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)