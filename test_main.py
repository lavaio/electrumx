#!/usr/bin/env python3.6
#
# Copyright (c) 2016-2018, Neil Booth
#
# All rights reserved.
#
# See the file "LICENCE" for information about the copyright
# and warranty status of this software.

'''Script to kick off the server.'''

import logging
import sys
import traceback

import electrumx.lib.tx as tx_lib

tests = [
    "02000000010000000000000000000000000000000000000000000000000000000000000000ffffffff04023e3300ffffffff0100405973070000001976a91402b6eb3eb965532c942f1c112c585716db12b06388ac00000000",
    "0200000001631e5ffb8895b2c25ede34b3851a0d94a152653018fd62d67d043b9099ea3638000000008a4730440220652056c409074e0288e04d52b20d2bbbff3d9995b6baa6321ee22273b8668d51022038558332bf0b54543375b68a994c06bd264e5b067c307536a578cc08dab15301012103bfe3595b7887b9912d401d15e6c78030a7317c66474048c50592821b6f82ad0c1f03ff8f00b17576a9140092169a02d4115764b1c7f13a383d66e60d48d688ac000000000129f17fd1570000001976a9140092169a02d4115764b1c7f13a383d66e60d48d688acec930000",
    "0100000000010126dd8dc7d2bfc9909072a92062b38b193ba73cd13c7e3ac6abaf58d489daf3b40100000000ffffffff0250c3000000000000220020a689d0b05d14328f9af0c28ff99dde1358fa4f71932aa117229eb0c03f64d637fa9e0c0000000000160014b361af90f02d454906041ce18a37aa3f4e6065c602483045022100b5db6bc8006d7dfe9a357ecade98f6e9eb265af4dd99731cbac475aa477b39b402202299c1f398f349b5604780625540063fa95521269f89d3907f7e7e3ebac8673501210369cd7ce319b6968ad725a60f1f0c5a3d4d44a9e3a72acf9620e2eb65d7a0b81c00000000",
    "0300000000030282469a545f5e2988053655945104545c2661301a7a95421eca2903fd5d5e9ab90200000000feffffff82469a545f5e2988053655945104545c2661301a7a95421eca2903fd5d5e9ab90000000000feffffff035f78c03b0000000017a914a4e83948c28c5db227204f178f2c69bbfc7824d187000000000000000000016a0101cd8b9bdffbdf7da3dbee56ccbd11d8d4deefe142f48e60fd0bc23674621c257f01000000174876e80000000000000000000017a91405260d20b1b667aafa4752d1e5028900df3a85c487010bc48b9a77e42d9a282942fc92764695efbb0ed1d9e2d0da33957de5ac2081b46209b0c85e2b043b07646a3a317c2642eeaf570fff83faaa841675146daca648a2d4036a7c9c13fd65b6fa76c27c491757cf83ede0633c696d37385018bac67d5d0eba02473044022054d2423e47f1aebbc9530adcd7983410c1530f896d4169a4c5808abf0ea93392022009a3c6447b979f90769c77d20dc00184edc50cc8ad8aacb01d5c7cfcf1ed63b30121034d7f1ba2c6b7ac272714fa82f196f60187a96b9f80d6c8299eabd33fdac913e502473044022068e61744ffcea1dafa8d059a9b6a1c05364213eec5a6595cc5899309916dee7a022067cd56d08eaf1e841ee14b1d61b0e696a02d5bb946340545ac1abcfe100d4af1012102334f9d82a23d283b212911b2358c918552068e49acf4ec0267668c8432d0506a00000000000000006302000339a8c2149d38a206cbfca4328389f3cd2e0b16efea1c6134344ade7b4ac69bd94823b2a90f5ff4ee7e81081dfd8b8c4be7158c1d1563ff77ad27c0892b5830265fedf4ad4cbe6a45033aae9e3058f4e9a2fbdb514b1a8d27e4c3003015664333fd4e10603300000000000000014bd7c501f26a9fc347e0effab918331a0f0a3aa19bd1895d1a3c604481e35792c87be4c3769b3b07703ae90bc3fa28df7d60328ccd191b598d3dcb48295b4da783938df26c131a31e6f5b6eeff1c35770ae08096e6938c120b844b116eb722d0cb865f56b9a82e4cca8db3fd661c560a175e95437a6d4ebb00403204e7c26b40ffc165d315dc511d979a2c429591624e6278130ae4c89423e2ceeab6377b571aafd4b29c3be790127945343cb5c65968e6ddd607ee6ccaaac5f515e888f175fa74b42c029cbe09c133ed56c558fd793b6cd114806f86c9d5dcebd1287dc9bc320cd488b98a556d4cc9da37f37dc504696750a84a95eeb83f6ad6d4a8f139e78029266b6397f9ad5e03207edcc5f5ca32582da103b47b792c9d59745b0c25ae139430d6626d9bf2177ac4b28d718ae0f549c2de436a5a965b46202af58bbb44ab719590d5a5d21df71c09ca57f2ff2fa8d220a5f8713691768b0eaaff159a9bd0766a7f7ea9531479c39ddb2caab56d87c8483f474b0e3908bde38d94978516fe4f627070048d63576837d48054bcf9493c348644bd302dd742dbfc6f4ed37fa45ba256ebe2b26aa7dde4f448de99e58a843111877657fb777293add00ad07fa73b60f741d95b8c36f8c18453c4dfdc874ddf72eec623c4974caf3c52b90312f017eb36e924c83ae380fe8cf8cfc385bcb985ba4eea355d675fb75d8bc38161bedcedfac41ba1abb2e5e993a1cad2adb314d556b6e95f997f21013b640e1f3316f441ac49a56e30b8cf0a04e03083581519866029e9d6e2c9857fdf511cc8d460115445b7281913f5a36fa49c2ccf3f8887a598f8faee89ddea5db5bd6a0a463ccfdcaca54618201f742385e44274f623e865dc6ae97273db3e0a69da84aec46d4e625afc55f222742eeecc176f0737cc7210eac207ad7f2394bb07c411d6f3cd2c70e1ee81ad6105d081a7838bb5b9f2b506e6c4f8230bf4c99d6c36bfd2869f872637d6616a57fc58b3b6a124c2b4e6d69d6c6bb0d046f875bccbc441710951b322def85450610be50bf5d0d2c8716d68ab2d2b0fac120a723eef68f21cba114349d3e30bb77c786f850ea4a42aa3571b56d24fc61277bde04b2c06dd8c173f0da8ac1f85e97420bc6d799616f48ece80418cc764be67764c6d578fde564cf61709bf92e087fd504f43a0e502b44625c03c93eaecea3d51982f3127669747574eb98ee6166f3596b81c68e86bff6b34b9ecefbd7372f82467bab16f2d4058ca827aeee5ac7247f3623926edc9058a4dfca854f5c2c32ae4614b19da98569b473d3bb84e4ceac6e46b21c4e072266fe3f6ed5e4385a37d6efeb118061d34f7e03ca880defbd5bfe5224e0b6ce33b8c93a8423b62cf5601744032b3192805a2b77f30261e1d56e2bd8b12ab3f89460c0505c3389c89fbe5c2ed454c92e0fd6ae60c577217ee87fc84b68d37d0246583cc3e2dfc2bf831d946760aacbe3ed8ee4b741bf9b95249406c6119230c56b65e63b67b319a52fc82d5b1d45561899535040dd90311f5f8433e04b2b3fe4e237b6f4c450e1dae597db7630fd7383f16c2055c441aa73f3230cad2fae3eacd67d686ef43c1cfb0c6b6abd53c26848104d23b6c9aa4cda9c991490381ddc1b27851ee15973ea32bbcab4b312377f38798be2eb79f123f109640e80812f5d672cd87cbbc6024fc16a3ab33d1fc4f8fb0c496e6e8db7fc4463686ba128fb31cdab4043a770c6e504e9ee50444da1e801a83efb650be1a49d3dadbf67748eaf27f2b1646778d65c2aa79684ced2ec7a8ab03469eb2e51d8104dc65faf632c7496fe826cc76ffc0bacb6724d6446a9e4043f199a2b52c1a9b72f7c7815760760a5e4ca470a02511269352c6dc1fab3a9d93f74439a9b4e8e4c429d8eab8e8fe00fa88aa7ede3d41eef8bf1d432eef7e6acddfd47fa852b5d8f9c5c38fdf96d817e3c7638a302b8d5abcd8b88b3298e02132ccd8657e9f96c4a7e5700e5bd17bf149485548e2a280d4a6a6e4aaaea2cc5a3e2429af8755befe7eb2159a623c9a57895dac18bb4185b10a428390e003b082408d83e5bd33b62e7eabcabd7de7238de47e2dcd80e8e6a66e736327cc026c513c2280ddbae25b78403ccd6fa83a375ffca69762d1995b449363d259dd4caf8ddbae082710be3d22ef9d0ecce123f73d7a085db3edb868c7eb24f7d20d784ee5239e7a369ec387bd716e15b7e54adfd3fbe309c14cd86cf212fc9eca03fe49b86d540efa866d166788e0013c2fde8a8f22b5c8e33af1e1206b1f0af59aec134429857dc5a23b122da648aa9f403716b8459d2f16ecc2610f23cd6d5d9ad3cfe18c15de5cdda8904974c530f52eb2f6dddc43f0af24f4695a01d170f5b8ac97a8b391085409c8aad21b5c9a68bd9a58b178f88527faae5c228872375d983cdcdecd1d572f658bdae85c63c73acd50091b46e7ffb44a32faca550a70ad3a7d8ecc137a858d3b2cc30d4643cf638256c04ab12a793bd03f87eec8c685befb84bd602d3fb1eae856ec408fe1884d47fa3574b8c97d5f153ae44351ba30c509d38c5aaba4624058f09e974a274a7c5b5a3e1516aa09ff2efaeaf681eca3219075d69d4c85fe0bfe1c9603fdc4bae8bc771d33cce8a47fa3022c47f6f9d85cc5f53f8ba8309760030a88003878c6cff0065c5d127e02cf0503022fe8f9171045d7cb5863bc071b1ac9ed3e2f3c97793610b110f652c798115ef205b4c8639e41d4ced44877384a1ebc53b71fe926e0e2de83877b8297cf9a127163072b98bd80c13d55660f7e084bfc45b3281880694e78c0a20311bb27ad717a9d9b3668387e1bc01ebeec659ad034e75341e3253a4af38c4a493298cba6f0b23289142117659b4a2ada9683a1d9df4a98b571d686108883889be008dfb068a27630bea741c540a435ee099491155627bb55b73bafd406b42294a42c7259e96433376fbbb7294030ee7b0433fe9e848e35c32630414ffc95b61a97cc752464404a0aebe2a8e292b6581d76a1dc426f94d60c08df78fd78ac08f5776893d5859f45668904bd5606d9cd06b0305bdee75acad37cbd4c8c1471abd12fde5599da6ddcb50ae7f0c6b9e64cd828e979ee8552b11e9d031cc198677b7a5854cf6cf2b11a80f4d4dfc55eeb3c5b15839e9f92a40d128da5484c7b84fe9e05de7420e556c97384e3b9a62f5afc7f407f1979d369ec03f399267739d06393b5d0a4c7a16fc14ef264d882297f4891e2ece9e45b5e65b69218513193a2e5fc3a8df20eef194382d3a522ac53fbaad974ef94670f6eea5984631c937ddc1194eab1afef6f772a510ee4a92259bbb42e09819ad22ddc5454d25ad250ecfd34d4b53de9beaf408eef2b9f8f3f14d8144481ebd07af3c35e6642760d83631e1073a879ac36b951d2dcc59980ecea01d30912232cc8237dc2e4d0708b5a77b047d5d2936666e41cc7ea05f960cfd503f742d5d764ffc5605c18a4b59eb1839f56ae8adfa9934d837dd7a83bc432d844e58a93ae876f750654d254176ec6eec340bb1a3e63b75fe2c452138e7140c3a4d13d6489bd92bff0cf465d3f0bfff3eec05defcd3a21d9113af165836967fa97dd4cdb85c87e86b998ee307be72ef0af01dd6e0733f1f956f31987ef5a8ecf7d7e405199747a335264468a6418835e784c33fed9713dbe0118a6ff90e31ad46425af3df639cf5f5e62b77d65a10f0bdfe99312efad2ab21e3df4b51633fd3668871efbdffeae2d0baec615c7a587ff83f1718c07d52bc0788fb35fe5bda71d2aa48a6347291eff023d63f1ac63dc005547b1edc42637e00c108e279c41fd0e51db0c37c10cd9f2078f4e90c9d400fdac06cf94ee24ce32a6dae17d13c02c2ba047d429754aa9c002e9e46c8cc1f680cce01d0fb5c56bc156fb91106600ed13022f574dba29a0c057010f3af15c734d88b33e7b88627da5a4babc2e923f7deb77d3f8f4da75c86a661b0b726de3bdfc3333183823d045f29e642c2b879981c178ac3d014f18de12ffa171a229d315af9a1bb62a7737a49b1c139afd182d23e29dfdc591a5f25404835bb7adecbae3fd4bd5c517a1f048876a8cebbc34cfb52ef1201e2d4c9249819f564d4d8aea879620e2bafbf0422015834ada5026eb33219d0e4f454c03ef91e33af964fccde97796ae58e0d6be3630fb5f9b40d95f7e77df51b999df7559204295d2c801cd3de15c91a2d4ceb7cbe983fce4cbd609a667b380fbf5c34a0f650b210361b485677e8778b7a2a18cc5dc6ce79d675f3586b985f14bd9d99cba04e9d9ca021d733f0f06db3a14eddfe93f651be7fdea4bee80813a986831dc1b0311d74ab69d6ab0357655a5fea2db5e028814f28368c079a23d212aedff9a3dbbdf456f0a52a51f1539fcdac0f629fb7ebc951a2655675ce1e16752dac81d2ffcc86865706588df18394f535f136912814eac7ea1b539d8a3d70629fa5ddd9ed0563be06b9679162b2d4d4c121db0bd9636708e751374642c6ab3d2285378cba81d634b8c39345e19a7c972234f92f753455f3acdd3aa66cbbdcb4f1c141453c11c984d70f2185aeb66db7b1af8e2167c73824822f4818bb4b4ac39168a839353663bc6e5b2c2bbf2aaa7d7d7e0506859820b3fce158a9acb674171d5afe41e1c1a4b754a2fee4dd7a059745b0ef9e1b13720e4ac279eb0beb47459ffbfb8bb8cee1d77956c7fd4f76bf5dfbb7df71b142c7d6a0d0168a030717db23c7b7562759e8014ac66a9cc2913a41938d44052ab7cb1731c1ae77e66f0650ee73f40c99cb18c1fa4c4fc1d4910fc11083cb5ca36d4e8609fa59ed55432d4febd3cf67646f1dad8771b7357b3abed91a3a9e525280e94da8ec8e5bbdb781668271c1a88fb40c2f63a7f4b095f43d05c916a3ca759aafc91d0f0a88dcf4515b35732d53731bed2c2c1662c5a6d65ae3f1546f4e06003913396f2e696641114a8c46b2b7dbc82f533799414a78b433b23fce9524ecaae865daf1916c77303819fd2f168b09eb02af5853a33bcee00814ec961814c5d8e97143f13ce80374d427d917a2bce963d52bc16172eeb690022089bf52841a9f3477c2f29d5d9c6a3de4a0b3606249d47920d0a527617a07eb97f81a3d803461e1e93b3f284640944adf799b5022ecc72f07db17fcbc119caba74293362bddcdfdff4e06be1492393bf92bb2be75263379908e47f0d6ed0c06f2cc6d9501b26a7c03af089fb767ab23c612391e6ab06a1ef76cc2d8110ad5ad71e8c2d110d7e4ad0e6996f8c0926bb0a8193190469aa0e43c3c4cba68c8d9646c0d0765fbf2b847bab79c7a9900760a61a4488ba2d0f29b5f10e94afa2def2b5246de25f058395f959b2c046f4bfebadbeb609f7f8f9a292306025506f6ea18371ba4d079574e28a484831bf9a6bc31e1d729a9a6c089e80100518ab9c65e8b90f978291133be22b11b0595169b9796d700949a44ab473bec71f7f8e48050553f3e93c2fdbb2a19c2a3af2a36ba724f45fb48bfea5e7ba3837f09d7f0069a667ca38433c17fdd49a5b6531dc93765577799c47a5e2a780f6e30248fc2750f77a00ea3dbae42de0032673dbe32510d72736ebdcbb6fe961b68b6750cf02ddabf599a8390772c1a9eefd6aa62eac351481cf4428a1754e4cb7bd1320ad3640ef2a9b88793eb80ab9883e9ec65af2f57736b37e5e6c145641982759ef5a6bd0babf4a4ce32d806a7f50ce00480f2e85a80f3785a1f2acd8d91458b6d14f2bf2396c2fa0541bd2250d1754ebec91414542c7d74640169c03771a9213f3acb439fb3add6abf8860d2250615628bb49067e3e3b4af911fecc7fd4ce9e5dd681aebf5ad0ffec2ac98fb7492b14c064835b7d2f06cb03d175fa0d0df00000000",
]

def test_tx_serialiazation():
    for test in tests:
        test = bytes.fromhex(test)
        deser = tx_lib.DeserializerLavaSegWit(test)
        tx = deser.read_tx()
        assert deser.cursor == len(test)
        #assert tx.serialize() == test

if __name__ == '__main__':
    test_tx_serialiazation()
 
