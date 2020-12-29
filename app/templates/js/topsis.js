function calcTOPSIS(result, tr, idNganh, year, arrayPriority, boiso) {

	/* INPUT*/
	// var year = "2017"
	// var idNganh = "KQ3"


	var rs = result[tr].nganh[idNganh].tuyen_sinh[year].danh_sach_dk;
	var cong_thuc = result[tr].nganh[idNganh].tuyen_sinh[year].cong_thuc;
	var chi_tieu = Math.ceil(result[tr].nganh[idNganh].tuyen_sinh[year].chi_tieu * boiso);
	var thang = result[tr].nganh[idNganh].tuyen_sinh[year].thang;
	var arrayResult = getArrayTD(rs, cong_thuc);

	//Tự tạo điểm chuẩn năm trước và điểm sàn
	var diemChuanNamTruoc = year !="2015"?result[tr].nganh[idNganh].tuyen_sinh[(parseInt(year) - 1) + ""].diem_chuan:8;
	var diem_san = 5;
	var buocNhay = 0.01;
	if (thang == 10) {
		diemChuanNamTruoc = diemChuanNamTruoc < 10 ? diemChuanNamTruoc : diemChuanNamTruoc / 3; 
	} else {
		//thang 30
		diemChuanNamTruoc = diemChuanNamTruoc > 10 ? diemChuanNamTruoc : diemChuanNamTruoc * 3
		diem_san = 13;
		buocNhay = 0.25;
	}


	arrayResult.sort(function(a, b) {
		return b.diem - a.diem
	})
	console.log(arrayResult)
	console.log("arrayPriority",arrayPriority)


	var diemDuChiTieu = getDiemDuChiTieu(arrayResult, chi_tieu, thang)
	var arrDataTopSis = [];

	var diem_xet_tuyen = diem_san;
	while (diem_xet_tuyen < diemDuChiTieu) {
		arrDataTopSis.push(
			{
				diem_xet_tuyen: diem_xet_tuyen,
				field: {
					diemTB: getDiemTB(diem_xet_tuyen, arrayResult),
					diemTBTheoNV: getDiemTBTheoNV(diem_xet_tuyen, arrayResult),
					doChenhLechDiemChuanNT: getDoChenhLechDiemChuanNT(diem_xet_tuyen, diemChuanNamTruoc),
					soLuongHocThuc: getSoLuongHocThucTheoChiTieu(diem_xet_tuyen, arrayResult)
				}
			})
		diem_xet_tuyen += buocNhay
	}
	// [22.15642857142857, 18.401035714285698, 0.5605864596808969, 237] (4)
	// 1 [22.15642857142857, 18.401035714285698, 0.5713669685209142, 237] (4)
	// 2 [22.15642857142857, 18.401035714285698, 0.5821474773609314, 237] (4)
	// 3 [22.15642857142857, 18.401035714285698, 0.5929279862009487, 237] (4)
	// 4 [22.15642857142857, 18.401035714285698, 0.6037084950409659, 237] (4)
	// 5 [22.15642857142857, 18.401035714285698, 0.6144890038809832, 237] (4)
	// 6 [22.15642857142857, 18.401035714285698, 0.6252695127210004, 238] (4)
	// 7 [22.15642857142857, 18.401035714285698, 0.6360500215610176, 238] (4)
	// 8 [22.15642857142857, 18.401035714285698, 0.6468305304010349, 238] (4)
	// 9 [22.15642857142857, 18.401035714285698, 0.6576110392410521, 240] (4)
	// 10 [22.15642857142857, 18.401035714285698, 0.6683915480810694, 244] (4)
	// 11 [22.15642857142857, 18.401035714285698, 0.6791720569210866, 248] (4)
	// 12 [22.15642857142857, 18.401035714285698, 0.6899525657611039, 250] (4)
	// 13 [22.15642857142857, 18.401035714285698, 0.7007330746011211, 253] (4)

	
	return TopSisAlgorithm(arrDataTopSis, arrayPriority, chi_tieu)
	/*output.twoResultSMax:[arrayData[s_max[0]], arrayData[s_max[1]]],
	twoResultSMin:[arrayData[s_min[0]],arrayData[s_min[1]]],
		twoResultC:[arrayData[c_max[0]],arrayData[c_max[1]]],*/
}


function TopSisAlgorithm(arrayData, arrayPriority, chiTieu) {
	var arrData = [];
	for (var i = 0; i < arrayData.length; i++) {
		var arr = [];
		arr.push(arrayData[i].field.diemTB);
		arr.push(arrayData[i].field.diemTBTheoNV);
		arr.push(arrayData[i].field.doChenhLechDiemChuanNT);
		arr.push(arrayData[i].field.soLuongHocThuc)
		arrData.push(arr)
	}

	var arrTS = [];
	arrTS.push(arrayPriority.diemTB)
	arrTS.push(arrayPriority.diemTBTheoNV)
	arrTS.push(arrayPriority.doChenhLechDiemChuanNT)
	arrTS.push(arrayPriority.soLuongHocThuc)


	/*---------------------------%
	 %    Buoc 1: Chuan hoa X    %
	 %---------------------------*/

	var arraySQRT = [0, 0, 0, 0]
	//Truong hop cang cao cang tot
	for (var i = 0; i < arrData[0].length - 1; i++) {
		for (var j = 0; j < arrData.length; j++) {
			arraySQRT[i] += arrData[j][i] * arrData[j][i];
		}
		arraySQRT[i] = Math.sqrt(arraySQRT[i])
	}

	// //Truong hop cang thap cang tot
	// for(var j=0;j<arrData.length;j++){
	// 	arraySQRT[3]+=1/((arrData[j][3]+.1)*(arrData[j][3]+.1));
	// }
	// arraySQRT[3] = Math.sqrt(arraySQRT[3])

	//TRuong hop khong don dieu
	var xo = chiTieu;
	var TT = 0;
	for (var j = 0; j < arrData.length; j++) {
		TT += ((arrData[j][3] - xo) * (arrData[j][3] - xo));

	}
	arraySQRT[3] = Math.sqrt(TT / arrData.length)

	// Tinh mang sau khi chuan hoa vecto
	var arrayNormalized = [];
	for (var i = 0; i < arrData.length; i++) {
		var arr = [];
		for (var j = 0; j < arrData[0].length; j++) {
			arr.push(0);
		}
		arrayNormalized.push(arr)
	}

	for (var i = 0; i < arrayNormalized[0].length - 1; i++) {
		for (var j = 0; j < arrayNormalized.length; j++) {
			arrayNormalized[j][i] = arrData[j][i] / arraySQRT[i]
		}
	}
	var TBP = 0;
	for (var j = 0; j < arrayNormalized.length; j++) {
		arrayNormalized[j][3] = (arrData[j][3] - xo) / arraySQRT[3]
		arrayNormalized[j][3] = Math.exp(-arrayNormalized[j][3] * arrayNormalized[j][3] / 2)
		TBP += arrayNormalized[j][3] * arrayNormalized[j][3]
	}
	for (var j = 0; j < arrayNormalized.length; j++) {
		arrayNormalized[j][3] = arrayNormalized[j][3] / Math.sqrt(TBP)

	}

	console.log("arrayNormalized")
	console.log(arrayNormalized)


	/*------------------------------------------%
	 %    Buoc 2: Tinh gia tri theo trong so    %
	 %------------------------------------------*/



	var arrTheoTrongSo = [];
	for (var i = 0; i < arrayNormalized.length; i++) {
		var arr = [];
		for (var j = 0; j < arrayNormalized[i].length; j++) {
			arr.push(arrayNormalized[i][j] * arrTS[j])
		}
		arrTheoTrongSo.push(arr)
	}


	console.log(arrTheoTrongSo)

	/*------------------------------------------%
	 %    Buoc 3: Bo sung giai phap ly tuong    %
	 %------------------------------------------*/
	var A_MAX = [0, 0, 0, 0];
	var A_MIN = [2, 2, 2, 2];
	for (var i = 0; i < arrTheoTrongSo[0].length; i++) {
		for (var j = 0; j < arrTheoTrongSo.length; j++) {
			if (arrTheoTrongSo[j][i] > A_MAX[i]) {
				A_MAX[i] = arrTheoTrongSo[j][i]
			}
			if (arrTheoTrongSo[j][i] < A_MIN[i]) {
				A_MIN[i] = arrTheoTrongSo[j][i]
			}
		}
	}
	console.log(A_MAX)
	console.log(A_MIN)
	/*-------------------------------------------------%
	 % Buoc 4: Tinh khoang cach toi giai phap ly tuong %
	 %-------------------------------------------------*/
	var S_MAX = [];
	var S_MIN = [];
	var C = []
	for (var i = 0; i < arrTheoTrongSo.length; i++) {
		var sum_MAX = 0;
		var sum_MIN = 0;
		for (var j = 0; j < arrTheoTrongSo[i].length; j++) {
			sum_MAX += Math.pow(arrTheoTrongSo[i][j] - A_MAX[j], 2)
			sum_MIN += Math.pow(arrTheoTrongSo[i][j] - A_MIN[j], 2)
		}
		S_MAX.push(Math.sqrt(sum_MAX))
		S_MIN.push(Math.sqrt(sum_MIN))

	}
	for (var i = 0; i < S_MAX.length; i++) {
		C.push(S_MIN[i] / (S_MAX[i] + S_MIN[i]))
	}

console.log(findMinKey([1,2,3,4,4,5,55,6,6,6,,6,77,9],5))
	console.log("C",C)
	console.log(findMaxKeys(C,5))
	console.log("s+",S_MAX)
	console.log(findMinKeys(S_MAX,5))
	console.log("s-",S_MIN)
	console.log(findMaxKeys(S_MIN,5))


	/*-----------------------------------------------%
	 % Buoc 5: Do do tuong tu toi giai phap ly tuong %
	 %-----------------------------------------------*/


	var s_max = findMinKeys(S_MAX,5);
	var s_min = findMaxKeys(S_MIN,5);
	var c_max = findMaxKeys(C,5);



	var output = {
		twoResultSMax:[],
		twoResultSMin:[],
		twoResultC:[],
	}
	console.log('test', s_max, s_min, c_max)
	output.twoResultSMax = s_max.map(function(i) {
		return arrayData[i]

	})
	output.twoResultSMin = s_min.map(function(i) {
		return arrayData[i]
	})
	output.twoResultC = c_max.map(function(i) {
		return arrayData[i]
	})
	console.log("========================================")
	console.log("========================================")
	console.log("========================================")
	console.log("========================================")
	console.log("========================================")
	console.log(s_max,s_min,c_max)
	console.log(output)
	return output

}


function getArrayTD(rsDiem, congthuc) {
	return rsDiem.map(function(i) {
		var m1 = i.m1;
		var m2 = i.m2;
		var m3 = i.m3;
		var dut = i.dut;
		var nv = i.nv;
		var diem = eval(congthuc)
		return {diem: diem, nv: nv};
	})
}
function getDiemDuChiTieu(arrayTD, chiTieu, thang) {

	var diemChiTieu = thang;
	var tongTSD = 0;
	for (var i = 0; i < arrayTD.length; i++) {
		if (arrayTD[i].diem < diemChiTieu) {
			diemChiTieu -= 0.1;
		}
		tongTSD++;
		if (tongTSD >= chiTieu) {
			return diemChiTieu
		}
	}
}
function getDiemTB(diemChuanDangXet, arrayTD) {
	var tongDiem = 0;
	var tongTS = 0;
	for (var i = 0; i < arrayTD.length; i++) {
		if (arrayTD[i].diem >= diemChuanDangXet) {
			tongDiem += arrayTD[i].diem;
			tongTS += 1;
		} else {
			return tongDiem / tongTS;
		}
	}
	return tongDiem / tongTS
}
function getDiemTBTheoNV(diemChuanDangXet, arrayTD) {
	var arrNV = [1, 1, 0.8, 0.75, 0.7, 0.65, 0.6, 0.55, 0.5, , 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]
	var tongDiem = 0;
	var tongTS = 0;
	for (var i = 0; i < arrayTD.length; i++) {
		if (arrayTD[i].diem >= diemChuanDangXet) {
			tongDiem += arrayTD[i].diem * arrNV[arrayTD[i].nv];
			tongTS += 1;
		} else {
			return tongDiem / tongTS;
		}
	}
	return tongDiem / tongTS
}
function getDoChenhLechDiemChuanNT(diemChuanDangXet, diemChuanNamTruoc) {

	return 1 - (Math.abs(diemChuanDangXet - diemChuanNamTruoc)) / diemChuanNamTruoc
}
function getSoLuongHocThucTheoChiTieu(diemChuanDangXet, arrayTD) {
	/*
	 CT f= 1/(1-b*DC/DT)*(a^NV) //NV tang, f giam, DT tang, f giam
	 */

	var a = 0.7;
	var tongTS = 0;
	var threshold = 0.175
	for (var i = 0; i < arrayTD.length; i++) {
		if (arrayTD[i].diem >= diemChuanDangXet) {
			if (arrayTD[i].nv == 1) {
				tongTS += 1;
			} else {
				tongTS += 1 / (arrayTD[i].diem - diemChuanDangXet + 1) * Math.pow(a, arrayTD[i].nv) > threshold ? 1 : 0
			}
		} else {
			return tongTS;
		}
	}
	return tongTS;
}


function findMaxKey(arr) {
	var max = 0;
	var key = -1;
	for (var i = 0; i < arr.length; i++) {
		if (arr[i] > max) {
			max = arr[i];
			key = i
		}
	}
	return key
}
function findMinKey(arr) {
	var min = 100;
	var key = -1;
	for (var i = 0; i < arr.length; i++) {
		if (arr[i] < min) {
			min = arr[i];
			key = i
		}
	}
	return key
}


function findMinKeys(arr,n) {
	var arrSort=[];
	for(var i=0;i<arr.length;i++){
		arrSort.push({value:arr[i],key:i})
	}
	arrSort.sort(function(a,b) {
		return a.value - b.value
	})
	var key =[];
	for(var j=0;j<n;j++){
		key.push(arrSort[j].key)
	}
	return key
}
function findMaxKeys(arr,n) {
	var arrSort=[];
	for(var i=0;i<arr.length;i++){
		arrSort.push({value:arr[i],key:i})
	}
	arrSort.sort(function(a,b) {
		return -a.value + b.value
	})
	var key =[];
	for(var j=0;j<n;j++){
		key.push(arrSort[j].key)
	}
	return key
}