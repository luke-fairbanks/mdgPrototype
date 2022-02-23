var modal = document.getElementById('editModal');
var iconBtn = document.getElementById('openEditFormIcon');
var picBtn = document.getElementById('openEditFormPicture');
var textBtn = document.getElementById('textBtn');
var span = document.getElementsByClassName("close")[0];

iconBtn.onclick = function() {
    modal.style.display = "block"
}
picBtn.onclick = function() {
    modal.style.display = "block"
}
textBtn.onclick = function(){
    modal.style.display = "block"
}


span.onclick = function() {
    modal.style.display = "none";
}

window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

var WalletConnect = window.WalletConnect.default;
var WalletConnectQRCodeModal = window.WalletConnectQRCodeModal.default

var walletConnector = new WalletConnect({
    bridge: 'https://bridge.walletconnect.org'
});
var uri = walletConnector.uri;
$('#wallet-connect-btn').on('click',function(){
    WalletConnectQRCodeModal.open(uri);
})


import bncOnboard from 'https://cdn.skypack.dev/bnc-onboard';

let web3;

var Web3 = window.Web3.default
//var Onboard = window.bncOnboard.default
const onboard = bncOnboard({
  dappId: '23a4ca89-79e5-435b-9dc7-ae5d1914d1b1',       // [String] The API key created by step one above
  networkId: 1,  // [Integer] The Ethereum network ID your Dapp uses.
  subscriptions: {
    wallet: wallet => {
       web3 = new Web3(wallet.provider)
    }
  },
  walletSelect: {
      wallets: [
        { walletName: "coinbase", preferred: true },
        { walletName: "trust", preferred: true },
        { walletName: "metamask", preferred: true },
        { walletName: "authereum" },
        { walletName: "walletLink", rpcUrl: "wss://mainnet.infura.io/ws/v3/8bc341c8b6b94dd59171587ca949f894", appName: "MDGprototype" }]
  }
});

await onboard.walletSelect();
await onboard.walletCheck();