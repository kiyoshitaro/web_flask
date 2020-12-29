var output;
$(window).load(function() {
    $.getJSON("./tuyensinh/test.json", function (result) {
        output = result;
    })
    .done(function() {
        testOnLoad();
    });
});

var id_truong, id_nganh, id_nam;
$('#truong').on('change', function() {
    var id = $(this).val();
    id_truong = id;
    if (id == "") {
        $('#nganh').text('');
        $('#nam').text('');
        return;
    }
    // $('.breadcrumb .child').text(output[id].ten_truong);
    var nganh = output[id].nganh;
    $('#nganh').html('<option value="">Chọn ngành</option>');
    for (var i in nganh) {
        $('#nganh').append("<option value='" + nganh[i].id_nganh + "'>" + nganh[i].ten_nganh + "</option>");
    }
});
$('#nganh').on('change', function() {
    var id = $(this).val();
    id_nganh = id;
    if (id == "") {
        $('#nam').text('');
        return;
    }
    var nams = output[id_truong].nganh[id].tuyen_sinh;
    $('#nam').html('<option value="">Chọn năm</option>');
    for (var nam in nams) {
        $('#nam').append("<option value='" + nam + "'>" + nam + "</option>");
    }
    var ds_dk = nams['2017'].danh_sach_dk;
    updatePhoDiem("#phodiem2017", phoDiem(ds_dk,0), 'Phổ điểm 2017');
    updatePhoDiem("#phodiem2016", phoDiem(nams['2016'].danh_sach_dk,0), 'Phổ điểm 2016');
    updatePhoDiem("#phodiem2015", phoDiem(nams['2015'].danh_sach_dk,0), 'Phổ điểm 2015');
    
});
var chitieu;
$('#nam').on('change', function() {
    var id = $(this).val();
    id_nam = id;
    if (id != "") {
        var ds_dk = output[id_truong].nganh[id_nganh].tuyen_sinh[id].danh_sach_dk;
        var num_dk = ds_dk.length;
        $('#tongso').text(num_dk);
        chitieu = output[id_truong].nganh[id_nganh].tuyen_sinh[id].chi_tieu;
        $('#chitieu').text(chitieu);

        updateDiemUuTien("#diemuutien", diemUuTien(ds_dk,0), 'Phân phối điểm ưu tiên trước xét tuyển');
        updateDiemUuTien("#diemuutienmoi", diemUuTien(ds_dk,27), 'Phân phối điểm ưu tiên sau xét tuyển');
    }
});

function runPara() {
    var a1 = parseInt($('#diemTB').val());
    var a2 = parseInt($('#diemTBTheoNV').val());
    var a3 = parseInt($('#doChenhLechDiemChuanNT').val());
    var a4 = parseInt($('#soLuongHocThuc').val());
    var bs = parseFloat($('#boiso').val());
    var sum_a = a1 + a2 + a3 + a4;
	var arrayPriority = {diemTB: a1/sum_a, diemTBTheoNV: a2/sum_a, doChenhLechDiemChuanNT: a3/sum_a, soLuongHocThuc: a4/sum_a};
	var outputTOPSIS = calcTOPSIS(output, id_truong, id_nganh, id_nam, arrayPriority, bs);
	showEmptyTOPSIS();
	showTOPSIS('#topsis1', outputTOPSIS.twoResultSMax);
	showTOPSIS('#topsis2', outputTOPSIS.twoResultSMin);
}

function showEmptyTOPSIS() {
    $('.table-score .tbody').html('');
    for (var i = 0; i < 5; i++) {
        $('.table-score .tbody').append(
            '<div class="row">'+
                '<div class="col-1">-</div>' +
                '<div class="col-2">-</div>' +
                '<div class="col-2">-</div>' +
                '<div class="col-2">-</div>' +
                '<div class="col-3">-</div>' +
                '<div class="col-2">-</div>' +
            '</div>');
    }
}

function showTOPSIS(id, arr) {
    $(id + ' .tbody').html('');
    console.log('eee' , arr);
    arr.forEach(function(item, index) {
        $(id + ' .tbody').append(
            '<div class="row">'+
                '<div class="col-1">' + (index + 1) + '</div>' +
                '<div class="col-2">' + item.diem_xet_tuyen.toFixed(2) + '</div>' +
                '<div class="col-2">' + item.field.diemTB.toFixed(2) + '</div>' +
                '<div class="col-2">' + item.field.diemTBTheoNV.toFixed(2) + '</div>' +
                '<div class="col-3">' + (item.field.doChenhLechDiemChuanNT*100).toFixed(2) + '%</div>' +
                '<div class="col-2">' + item.field.soLuongHocThuc + '/' + chitieu + '</div>' +
            '</div>');
    });
}

function phoDiem(arr, ther) {
    var rs = [];
    for (var i = 0; i<30; i++) {
        rs.push({y: 0, label: i});
    }
    var index;
    for (i in arr) {
        sum = arr[i].dut + arr[i].m1 + arr[i].m2 + arr[i].m3;
        if (sum > 30) sum = 30
        index = Math.ceil(sum) - 1;
        rs[index].y+=1;
    }
    return rs;
}

Chart.defaults.global.defaultFontSize = 10;
function showPhoDiem(id, pd, title) {
    var ctx = $(id + ' canvas').get(0).getContext("2d");
    new Chart( ctx, {
        type: 'bar',
        data: {
            labels: pd.map(function(i){ return i.label}),
            datasets: [{
                data: pd.map(function(i){ return i.y}),
                backgroundColor: 'rgba(116, 36, 165, 0.5)',
            }]
        },
        options: {
            responsive: true,
            legend: {
                display: false,
            },
            title: {
                display: title ? true : false,
                text: title,
                fontSize: 14
            }
        }
    });
}

function updatePhoDiem(id, pd, title) {
    // chart.data = {datasets: [{
    //     data: pd.map(function(i){ return i.y}),
    //     backgroundColor: 'rgba(116, 36, 165, 0.5)',
    // }]};
    // chart.update();
    // myLineChart = new Chart(ctx).Line(jsonData, {
    //     responsive: true,
    //     bezierCurveTension : 0.3
    // });
    $(id + ' canvas').remove(); // this is my <canvas> element
    $(id).append('<canvas><canvas>');
    showPhoDiem(id, pd, title);
}

function diemUuTien(arr, ther) {
    var rs = [];
    for (var i = 0; i<8; i++) {
        rs.push({y: 0, label: "+" + (i/2)});
    }
    var index;
    for (i in arr) {
        if (arr[i].dxt < ther) continue;
        index = Math.ceil(arr[i].dut * 2);
        rs[index].y+=1;
    }
    return rs;
}

function showDiemUuTien(id, pd, title) {
    var ctx = $(id + ' canvas').get(0).getContext("2d");
    new Chart( ctx, {
        type: 'pie',
        data: {
            labels: pd.map(function(i){ return i.label}),
            datasets: [{
                data: pd.map(function(i){ return i.y}),
                backgroundColor: pd.map(function(i, index){ return 'rgba(116, 36, 165, ' + (1-(index+1)/10) + ')'}),
            }]
        },
        options: {
            responsive: true,
            legend: {
                position: 'right'
            },
            title: {
                display: title ? true : false,
                text: title,
                fontSize: 14
            }
        }
    });
}

function updateDiemUuTien(id, pd, title) {
    // chart.data = {datasets: [{
    //     data: pd.map(function(i){ return i.y}),
    //     backgroundColor: pd.map(function(i, index){ return 'rgba(116, 36, 165, ' + (1-(index+1)/10) + ')'}),
    // }]};
    // chart.update();

    $(id + ' canvas').remove(); // this is my <canvas> element
    $(id).append('<canvas><canvas>');
    showDiemUuTien(id, pd, title);
}

function testOnLoad() {
    showEmptyTOPSIS();
    for (var i in output) {
        $('#truong').append("<option value='" + output[i].id_truong + "'>" + output[i].ten_truong + "</option>")
    }
    // var _ds_dk = output['BKA'].nganh['KT22'].tuyen_sinh['2017'].danh_sach_dk;
    // showPhoDiem('#phodiem2017', phoDiem(_ds_dk,0), 'Phổ điểm 2017');
    // showPhoDiem('#phodiem2016', phoDiem(_ds_dk,0), 'Phổ điểm 2016');
    // showPhoDiem('#phodiem2015', phoDiem(_ds_dk,0), 'Phổ điểm 2015');
    // showDiemUuTien('#diemuutien', diemUuTien(_ds_dk,0), 'Phân phối điểm ưu tiên trước xét tuyển');
    // showDiemUuTien('#diemuutienmoi', diemUuTien(_ds_dk,7), 'Phân phối điểm ưu tiên sau xét tuyển');
}