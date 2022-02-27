var modal = document.getElementById('editModal');
var iconBtn = document.getElementById('openEditFormIcon');
var picBtn = document.getElementById('openEditFormPicture');
var textBtn = document.getElementById('textBtn');
var span = document.getElementsByClassName("close")[0];
var trashModal = document.getElementById('trash-modal');


if (iconBtn != null){
    iconBtn.onclick = function() {
        modal.style.display = "block"
    }
}
if (picBtn != null){
    picBtn.onclick = function() {
        modal.style.display = "block"
    }
}
if (textBtn != null){
    textBtn.onclick = function(){
        //modal.style.display = "block"
        $(modal).css("display","block")
    }
}
if (span != null){
    span.onclick = function() {
        modal.style.display = "none";
        trashModal.style.display = "none";

    }
}
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
        trashModal.style.display = "none";

    }
}

/*$('window').ready(function(){
    $('.card').removeClass('is-loading')
})*/
$('.card').on('click', function () {  
    $(this).toggleClass('flipped');
});

//$('.card').draggable()
//$(".assets").sortable()
//SORT THE CARDS

$('.modal').click(function(e){
    e.stopPropagation();
})
$('.user-direct-btn').click(function(e){
    e.stopPropagation();
})

$('.asset-trash').on('click', function(e){
    e.stopPropagation();
    $(this).next().css("display","block");
    $(this).closest(".modal").css("cursor",'default')
    $('.close').click(function(e){
        e.stopPropagation();
        $(this).closest(".modal").css("display",'none')

    })
    $('.cancelDelete').click(function(e){
        e.stopPropagation()
        $(this).closest(".modal").css("display",'none')
        $(this).closest(".modal").css("cursor",'pointer')

    })
    $('.confirmDelete').click(function(){
        var assetid = $(this).attr('id')
        $(this).closest(".card-wrapper").css("display",'none');
        var asset_data =[
            {"AssetId": assetid},
            {"AssetShow": 'none'},
            {"AssetDelete": true }
        ]
        $.ajax({
            type:"POST",
            url:'/assetpost',
            data: JSON.stringify(asset_data),
            contentType: "application/json",
            dataType: 'json',
            success: function(result) {
                console.log(result);
            }
        })
    
    })
})


$('.show-checkbox').click(function(e){
    $(this).parents().toggleClass('darken-card')
    var assetid = $(this).attr('id')
    var assetshow = $(this).is(":checked")
    var asset_data =[
        {"AssetId":assetid},
        {"AssetShow":assetshow},
        {"AssetDelete": false }

    ]
    $.ajax({
        type:"POST",
        url:'/assetpost',
        data: JSON.stringify(asset_data),
        contentType: "application/json",
        dataType: 'json',
        success: function(result) {
            console.log(result)
        }
    })
});

/*var WalletConnect = window.WalletConnect.default;
var WalletConnectQRCodeModal = window.WalletConnectQRCodeModal.default

var walletConnector = new WalletConnect({
    bridge: 'https://bridge.walletconnect.org'
});
var uri = walletConnector.uri;
$('#wallet-connect-btn').on('click',function(){
    WalletConnectQRCodeModal.open(uri);
})
*/

import bncOnboard from 'https://cdn.skypack.dev/bnc-onboard';

let web3;

const RPC_URL = "wss://mainnet.infura.io/ws/v3/8bc341c8b6b94dd59171587ca949f894"
const APP_NAME = "MDGPrototype"
const INFURA_KEY = "8bc341c8b6b94dd59171587ca949f894"

var Web3 = window.Web3.default
//var Onboard = window.bncOnboard.default
const onboard = bncOnboard({
  dappId: '23a4ca89-79e5-435b-9dc7-ae5d1914d1b1',       // [String] The API key created by step one above
  networkId: 1,  // [Integer] The Ethereum network ID your Dapp uses.
  subscriptions: {
    wallet: wallet => {
       web3 = new Web3(wallet.provider)
       console.log(`${wallet.name} is now connected!`)
    }
  },
  walletSelect: {
      wallets: [
        //{ walletName: "coinbase", preferred: true },
        { walletName: "trust", preferred: true, rpcUrl: RPC_URL, },
        { walletName: "metamask", preferred: true },
        { walletName: "authereum" },
        { walletName: "walletLink", rpcUrl: RPC_URL, appName: APP_NAME, preferred: true },
        {
            walletName: "walletConnect",
            infuraKey: INFURA_KEY,
            preferred: true
          },
        ]
  }
});

const readyToTransact = async () => {
    if (!provider) {
      const walletSelected = await onboard.walletSelect()
      if (!walletSelected) return false
    }

    const ready = await onboard.walletCheck()
    return ready
  }
$('#wallet-connect-btn').on('click', async function(){
    await onboard.walletSelect();
    await onboard.walletCheck();

})
$('#wallet-check-btn').on('click',function(){
    onboard.walletCheck()
})
