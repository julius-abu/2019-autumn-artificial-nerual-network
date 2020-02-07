import matplotlib.pyplot as plt
import numpy as np


def plot_loss_and_acc(loss_and_acc_dict):
	fig = plt.figure()
	tmp = list(loss_and_acc_dict.values())
	maxEpoch = len(tmp[0][0])
	stride = np.ceil(maxEpoch / 10)

	maxLoss = max([max(x[0]) for x in loss_and_acc_dict.values()]) + 0.1
	minLoss = max(0, min([min(x[0]) for x in loss_and_acc_dict.values()]) - 0.1)

	for name, lossAndAcc in loss_and_acc_dict.items():
		plt.plot(range(1, 1 + maxEpoch), lossAndAcc[0], '-s', label=name)

	plt.xlabel('Epoch')
	plt.ylabel('Loss')
	plt.legend()
	plt.xticks(range(0, maxEpoch + 1, 2))
	plt.axis([0, maxEpoch, minLoss, maxLoss])
	plt.show()


	maxAcc = min(1, max([max(x[1]) for x in loss_and_acc_dict.values()]) + 0.1)
	minAcc = max(0, min([min(x[1]) for x in loss_and_acc_dict.values()]) - 0.1)

	fig = plt.figure()

	for name, lossAndAcc in loss_and_acc_dict.items():
		plt.plot(range(1, 1 + maxEpoch), lossAndAcc[1], '-s', label=name)

	plt.xlabel('Epoch')
	plt.ylabel('Accuracy')
	plt.xticks(range(0, maxEpoch + 1, 2))
	plt.axis([0, maxEpoch, minAcc, maxAcc])
	plt.legend()
	plt.show()



if __name__ == '__main__':
	loss = [x for x in range(10, 0, -1)]
	acc = [x / 10. for x in range(0, 10)]

	gru_tr_acc = [0.36434925, 0.39747191, 0.41573034, 0.44042603, 0.45622659, 0.47729401, 0.49543539, 0.51345974, 0.54822097, 0.56601124,
				  0.58988764, 0.60697566, 0.63307584, 0.65507959, 0.69487360, 0.71231273, 0.74754213, 0.77083333, 0.79412453, 0.83087547]
	gru_tr_loss= [0.09333299, 0.08690859, 0.08410398, 0.08145366, 0.07948889, 0.07657586, 0.07454562, 0.07106124, 0.06835590, 0.06563845,
	              0.06270546, 0.06015539, 0.05629059, 0.05374622, 0.04823478, 0.04505566, 0.04017930, 0.03647410, 0.03279589, 0.02815036]
	gru_val_acc= [0.36421435, 0.38782925, 0.41326067, 0.37965486, 0.41689373, 0.42506812, 0.42688465, 0.43505904, 0.38328792, 0.41780200,
	 			  0.43869210, 0.38510445, 0.41326067, 0.41235241, 0.41780200, 0.41235241, 0.39327884, 0.39872843, 0.39872843, 0.41961853]
	gru_val_loss=[0.09398228, 0.08765966, 0.08350776, 0.08492478, 0.08503743, 0.08441493, 0.09045265, 0.08511495, 0.09480916, 0.08698131,
				  0.08870826, 0.10537756, 0.10061624, 0.10668855, 0.11168271, 0.11143873, 0.13455471, 0.14049394, 0.14154738, 0.15872202]

	lstm_tr_acc=[0.37066947565543074, 0.4110486891385768, 0.4204119850187266, 0.43644662921348315, 0.44241573033707865, 0.4639513108614232, 0.4734316479400749, 0.4841994382022472, 0.5024578651685393, 0.5127574906367042, 0.5280898876404494, 0.5369850187265918, 0.5555945692883895, 0.5699906367041199, 0.59187734082397, 0.5981975655430711, 0.6274578651685393, 0.6525046816479401, 0.6748595505617978, 0.6942883895131086, 0.7195692883895131, 0.7488295880149812, 0.7737593632958801, 0.7914325842696629, 0.8112125468164794, 0.836376404494382, 0.8522940074906367, 0.8759363295880149, 0.8923220973782772, 0.9104634831460674, 0.9177200374531835, 0.9316479400749064, 0.9433520599250936, 0.9561095505617978, 0.9600889513108615, 0.9757724719101124, 0.975187265917603, 0.9838483146067416, 0.9897003745318352, 0.9955524344569289]

	lstm_tr_loss=[0.09109024180287725, 0.08512076237395907, 0.08293718974409478, 0.08097182886765691, 0.07965646042359456, 0.07735415686912528, 0.07604251324097985, 0.07398637157449785, 0.07251167833135369, 0.07082684445526269, 0.06929263438373692, 0.0675611025706101, 0.06555925324656879, 0.06340028601611375, 0.06086412151012751, 0.05909181608075506, 0.05612712105115255, 0.0532069971282663, 0.0498168868246429, 0.047390938659760164, 0.043842243550394136, 0.04000332234915667, 0.03620062626668074, 0.03345853926558117, 0.03066391432099742, 0.026734747730321095, 0.024008693386737803, 0.020740201015702068, 0.018474991891571504, 0.016045346314153785, 0.014619157080144416, 0.012543710680505827, 0.010755377776605995, 0.008762107460501461, 0.008058362108014772, 0.005660799574712989, 0.00545413950983564, 0.00434519209642197, 0.0033182873315838854, 0.0022639918869970825]

	lstm_val_acc=[0.3605812897366031, 0.3905540417801998, 0.4187102633969119, 0.4287011807447775, 0.4214350590372389, 0.44323342415985467, 0.4332425068119891, 0.40599455040871935, 0.4296094459582198, 0.4477747502270663, 0.410535876475931, 0.4178019981834696, 0.4296094459582198, 0.4477747502270663, 0.4396003633060854, 0.4232515894641235, 0.4114441416893733, 0.43142597638510444, 0.4296094459582198, 0.40054495912806537, 0.40962761126248864, 0.4223433242506812, 0.4087193460490463, 0.3869209809264305, 0.4114441416893733, 0.43142597638510444, 0.3941871026339691, 0.40599455040871935, 0.40417801998183467, 0.3905540417801998, 0.4214350590372389, 0.4196185286103542, 0.41689373297002724, 0.40054495912806537, 0.410535876475931, 0.40054495912806537, 0.4123524069028156, 0.3923705722070845, 0.39146230699364215, 0.4159854677565849]

	lstm_val_loss=[0.09224902950125755, 0.08670217876105174, 0.08471305704896391, 0.08326828609695226, 0.08375208893220713, 0.08107622063885377, 0.08391972426172822, 0.0868722603713026, 0.08741332248164566, 0.08137244684494808, 0.08381107679613063, 0.08750931968697627, 0.08176954284134397, 0.08449962629609277, 0.08721709061924919, 0.0894204736513836, 0.09566219506969677, 0.10176467695201559, 0.10460241927979319, 0.108888280922234, 0.11072969858912746, 0.11775557367938091, 0.12564606892856872, 0.1322570255298597, 0.13898838502942812, 0.15017876610985462, 0.17230473054094167, 0.16560437070792855, 0.18352842991401888, 0.19265554668034995, 0.21520070072524014, 0.2111986473838813, 0.2234111979915054, 0.22988547930167438, 0.23667640755330294, 0.24520754889939506, 0.26396433414923504, 0.26795621214943727, 0.28622085153785864, 0.29177689400724016]
	

	rnn_tr_acc=[0.36727528, 0.43574438, 0.48724251, 0.52984551, 0.58883427, 0.64618446, 0.70962079, 0.76942884, 0.82666199, 0.86598783,
			    0.90215356, 0.92626404, 0.94405431, 0.96090824, 0.97155899, 0.98314607, 0.98841292, 0.99403090, 0.99918071, 0.99976592]
	rnn_tr_loss=[0.09039508, 0.08067009, 0.07544826, 0.06974897, 0.06269045, 0.05511823, 0.04657118, 0.03744543, 0.02972180, 0.02302507, 
				 0.01788560, 0.01377746, 0.01108333, 0.00835336, 0.00640659, 0.00464720, 0.00332140, 0.00230614, 0.00105791, 0.00065383]
	rnn_val_acc=[0.41235241, 0.41326067, 0.42597639, 0.38237965, 0.38328792, 0.42688465, 0.40690282, 0.37057221, 0.38147139, 0.36966394, 
				 0.37511353, 0.37602180, 0.38147139, 0.39146231, 0.37874659, 0.37693006, 0.37783833, 0.38419619, 0.38419619, 0.39237057]
	rnn_val_loss=[0.08690231, 0.08552199, 0.08374582, 0.08979701, 0.09252759, 0.10363620, 0.12236758, 0.12822073, 0.14241018, 0.15072513, 
				  0.16473825, 0.18105707, 0.19027419, 0.21033378, 0.21471091, 0.22075824, 0.22568925, 0.23960282, 0.24096264, 0.24633482]

	lstm_noatt_tr_acc = [0.31448970037453183, 0.37909644194756553, 0.39864232209737827, 0.4166666666666667, 0.4243913857677903, 0.4330524344569288, 0.44300093632958804, 0.4481507490636704, 0.4559925093632959, 0.4602059925093633, 0.46640917602996257, 0.47401685393258425, 0.47752808988764045, 0.48993445692883897, 0.49461610486891383, 0.4948501872659176, 0.504564606741573, 0.5108848314606742, 0.5159176029962547, 0.53125, 0.5301966292134831, 0.5424859550561798, 0.5557116104868914, 0.5574672284644194, 0.5687031835205992, 0.5756086142322098, 0.5839185393258427, 0.5946863295880149, 0.5987827715355806, 0.6034644194756554, 0.622308052434457, 0.6315543071161048, 0.6427902621722846, 0.6505149812734082, 0.6633895131086143, 0.6712312734082397, 0.6830524344569289, 0.6990870786516854, 0.7024812734082397, 0.7134831460674157]

	lstm_noatt_tr_loss = [0.0967447565875473, 0.09032874126057053, 0.08684305020709163, 0.08438486321951343, 0.08264645613897383, 0.08131692040893022, 0.07991012864596166, 0.07906683086511794, 0.07807924763093727, 0.07707531305818299, 0.07639281994450405, 0.07565308558276754, 0.07457279542998205, 0.07389026592147262, 0.07274813760309183, 0.0724874556985464, 0.07125879322572817, 0.0707707865938042, 0.06981337158365196, 0.06829937915090988, 0.06746627686175515, 0.06639944610607981, 0.06507118490667602, 0.06483446466230722, 0.06394468443224047, 0.06189357969309953, 0.06119621019070961, 0.059504543232281555, 0.05942962324937408, 0.05829294744446483, 0.0558677747329411, 0.05515243618466546, 0.053186518133161, 0.0525848035411107, 0.05072382455935862, 0.049286273123229044, 0.047859165179176946, 0.04603143949724371, 0.04553326108747542, 0.0438518812984563]

	lstm_noatt_val_acc = [0.36693914623069934, 0.3869209809264305, 0.405086285195277, 0.40599455040871935, 0.38782924613987285, 0.40236148955495005, 0.4150772025431426, 0.39691189827429607, 0.4187102633969119, 0.40236148955495005, 0.40417801998183467, 0.4141689373297003, 0.40236148955495005, 0.4150772025431426, 0.42779291553133514, 0.4250681198910082, 0.410535876475931, 0.4123524069028156, 0.43142597638510444, 0.4332425068119891, 0.4159854677565849, 0.43415077202543145, 0.41326067211625794, 0.4187102633969119, 0.4141689373297003, 0.4214350590372389, 0.4069028156221617, 0.42779291553133514, 0.42779291553133514, 0.4123524069028156, 0.3923705722070845, 0.4114441416893733, 0.4159854677565849, 0.4196185286103542, 0.4114441416893733, 0.41689373297002724, 0.4159854677565849, 0.40054495912806537, 0.405086285195277, 0.405086285195277]

	lstm_noatt_val_loss = [0.09384581276116644, 0.08795012202076648, 0.08583289552666078, 0.08473194663249613, 0.0844459869881092, 0.0838113897069815, 0.08420759109233748, 0.08433058476253166, 0.08360424169510955, 0.08495373676085234, 0.08475197135698351, 0.08286559581756592, 0.08692138169052166, 0.08745613252975852, 0.08686029526669799, 0.08277501819569019, 0.08434994338751922, 0.08796200229296568, 0.08576214069891366, 0.08715861873340866, 0.08494989358761655, 0.08854809996217733, 0.0926987214807377, 0.09155499014824114, 0.09056767894396665, 0.09656517192734901, 0.09189609118096943, 0.09326259490038243, 0.0941413261476806, 0.0982770068227541, 0.10715622516462307, 0.09986998144872182, 0.10555580347695208, 0.10368374371723518, 0.1110091816285434, 0.10969037158612659, 0.11564977752631843, 0.11768037259416295, 0.13109185579795388, 0.12625842783041805]

	# plot_loss_and_acc({'with attention training': [lstm_tr_loss, lstm_tr_acc],
	# 					'with attention dev': [lstm_val_loss, lstm_val_acc],
	# 				   'without attention training' : [lstm_noatt_tr_loss, lstm_noatt_tr_acc],
	# 				   'without attention dev' : [lstm_noatt_val_loss, lstm_noatt_val_acc] })
	# plot_loss_and_acc({'RNN training': [rnn_tr_loss, rnn_tr_acc],
	# 					'RNN dev': [rnn_val_loss, rnn_val_acc],
	# 				   'LSTM training' : [lstm_tr_loss[0:20], lstm_tr_acc[0:20]],
	# 				   'LSTM dev' : [lstm_val_loss[0:20], lstm_val_acc[0:20]],
	# 				    'GRU training' : [gru_tr_loss, gru_tr_acc],
	# 				   'GRU dev' : [gru_val_loss, gru_val_acc]})
	plot_loss_and_acc({'training': [lstm_tr_loss[0:20], lstm_tr_acc[0:20]],
						'dev': [lstm_val_loss[0:20], lstm_val_acc[0:20]]
						})
	print(lstm_tr_loss[19], lstm_tr_acc[19])