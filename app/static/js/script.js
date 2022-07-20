listInput = []

resumeQua = document.getElementsByClassName("resQua");
resumeItem = document.getElementsByClassName("item");

isEditing()

function showResumen(id) {
  if (isAnyValue()) {
    document.getElementById(id).style.display = 'flex';
  } else {
    showFlash()
  }
}
function hideResumen(id) {
  //dumpValuesToList();
  document.getElementById(id).style.display = 'none';
}
function hideFather(element) {
  listInput = document.getElementsByClassName("listInput");
  idinfo = document.getElementsByClassName("idinfo");

  father = element.parentNode;
  father.style.display = 'none';
  father.querySelector('.resQua').innerHTML = "";
  father.querySelector('.fQuan').value = "";


  resId = father.querySelector('.id').value

  for (let i = 0; i < idinfo.length; i++) {
    if (resId == idinfo[i].value) {
      
      listInput[i].value = ""
    }
  }
  calcTotal();

}
function dumpValuesToRes() {
  listInput = document.getElementsByClassName("listInput")

  resumeUnitPrice = document.getElementsByName("unit_price")
  resumeBulkPrice = document.getElementsByName("bulk_price")

  resumeVisiblePrice = document.getElementsByClassName("resprice")

  resumeQua = document.getElementsByClassName("resQua")
  resumeTotal = document.querySelectorAll(".total")

  resumeW = document.querySelectorAll(".weight")
  resumeWt = document.querySelectorAll(".weightype")
  resumetotalW = document.querySelectorAll(".totalw")

  bulkswitch = document.querySelectorAll(".listSwitch")
  bulk = document.querySelectorAll(".bu")

  //try to hide the first visible .item
  why = 1
  
  for (let i = 0; i < listInput.length; i++) {
    
    quantity = Number( listInput[i].value )

    if ( quantity && quantity > 0) {
      
      if ( why ) {
        resumeItem[i].style.border = "none"
        why = 0
      }
      
      w = Number(resumeW[i].innerHTML)
      wt = resumeWt[i].innerHTML
      finalqua = quantity
      mayorPrice = resumeBulkPrice[i].value / Number( bulk[i].value )

      if ( quantity >= Number( bulk[i].value )){
        price = mayorPrice
      }
      else{
        price = resumeUnitPrice[i].value
      }
      // if BULKSWITCH IS NOT CHECKED SET BULK PRICE
      if ( !bulkswitch[i].checked ) {
        finalqua = quantity * Number(bulk[i].value);
        price = mayorPrice;
      }
      
      resumeVisiblePrice[i].innerHTML = price
      resumeQua[i].innerHTML = finalqua
      resumeTotal[i].innerHTML = (price * finalqua).toLocaleString();
      resumetotalW[i].value = calcWeight(w, wt, finalqua)

      resumeItem[i].style.display = "grid";

    } else {
      resumeItem[i].style.display = "none";
      resumeQua[i].innerHTML = "";
    }
  }
  calcTotal();
}
/*function dumpValuesToList(){
  listInput = document.getElementsByClassName("listInput");
  resumeInput = document.getElementsByClassName("resInput");
  
  for (let i = 0; i < listInput.length; i++){
    listInput[i].value = resumeInput[i].value
  } 
}
*/
function queryOrder(el) {
  dumpValuesToRes();
  dumpFormValues();
  showResumen(el);
}
function calcWeight(weight, type, qua) {
  if (type == 'Kg' || type == 'L') { weight = weight * 1000 }
  return weight * qua
}
function redu(weight) {
  type = 'g'
  len = weight.toString().length
  if (len >= 4) {
    weight = weight / 1000
    type = 'Kg'
    if (len >= 7) {
      weight = weight / 1000
      type = 'T'
    }
  }
  return [weight, type]
}
function calcTotal() {
  resumeQua = document.getElementsByClassName("resQua");

  resumeTotal = document.querySelectorAll(".total")
  resumetotalW = document.querySelectorAll(".totalw")

  total = 0
  totalw = 0

  for (let i = 0; i < resumeTotal.length; i++) {
    qua = Number(resumeQua[i].innerHTML)
    if (qua && qua > 0) {
      x = resumeTotal[i].innerHTML.replaceAll('.', '');
      n = Number(x.replaceAll(',', ''));
      w = Number(resumetotalW[i].value);
      total += n;
      totalw += w;

    }
  }

  data = redu(totalw)


  document.getElementById("totaltotal").innerHTML = total.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".")

  document.getElementById("totalweight").innerHTML = Math.round(data[0] * 10) / 10
  document.getElementById("totalweight").title = totalw + "g"

  document.getElementById("totalwt").innerHTML = " "+data[1]
}
function dumpFormValues() {

  resQuan = document.querySelectorAll(".resQua")

  resTotal = document.getElementById("totaltotal")
  resTotalW = document.getElementById("totalweight")
  resTotalWt = document.getElementById("totalwt")

  inQuan = document.getElementsByClassName("fQuan");

  resPrice = document.getElementsByClassName("resprice");
  inPrice = document.getElementsByClassName("form_final_price")  

  inFtt = document.getElementById("ftt");
  inFtw = document.getElementById("ftw");

  for (let i = 0; i < resQuan.length; i++) {
    q = Number(resQuan[i].innerHTML)
    if (q) {
      inQuan[i].value = q
      inPrice[i].value = resPrice[i].innerHTML
    }
  }
  inFtt.value = resTotal.innerHTML
  inFtw.value = resTotalW.innerHTML + " " + resTotalWt.innerHTML
}
function showAdv(id) {
  adv = document.getElementById("adv_" + id)
  adv.style.display = "flex";
}
function hideAdv(id) {
  adv = document.getElementById("adv_" + id)
  adv.style.display = "none";
}
function showAdder() {
  document.getElementById("adder_cont").style.display = "flex";
}
function hideAdder() {
  document.getElementById("adder_cont").style.display = "none";
}
function isEditing() {
  try {
    is_editing = document.getElementById("typo").value

    if (is_editing) {
      showAdder()
    }
  } catch (error) { }
}
function isAnyValue() {
  listInput = document.getElementsByClassName("listInput");
  for (let i = 0; i < listInput.length; i++) {
    value = listInput[i].value
    if (value && value > 0) {
      return true
    }
  }
  return false
}
function showLastDetail() {
  dumpToDetail();
  showFlash();

  document.getElementById("lastdetail").style.display = "flex";
}
function getDateTime() {
  var t = new Date();
  var time = t.getHours() + ":" + t.getMinutes();
  var date = t.getFullYear() + '-' + (t.getMonth() + 1) + '-' + t.getDate();
  var value = date + ' ' + time;
  return value
}
function showFlash() {
  document.getElementById("noproduct").style.display = "flex";
}
function hideFlash( el ) {
  document.getElementById("noproduct").style.display = "none";
}
function toggle( id ){
  document.getElementById( id ).classList.toggle("show")
}
function changePrice( product_id ){
  toggle( "unit_price_"+product_id )
  toggle( "bulk_price_"+product_id )
}