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

//import WalletConnect from "./node_modules/@walletconnect/client"
//import QRCodeModal from "./node_modules/@walletconnect/qrcode-modal";

// Create a connector
const connector = new WalletConnect({
  bridge: "https://bridge.walletconnect.org", // Required
  qrcodeModal: QRCodeModal,
});

// Check if connection is already established
if (!connector.connected) {
  // create new session
  connector.createSession();
}

// Subscribe to connection events
connector.on("connect", (error, payload) => {
  if (error) {
    throw error;
  }

  // Get provided accounts and chainId
  const { accounts, chainId } = payload.params[0];
});

connector.on("session_update", (error, payload) => {
  if (error) {
    throw error;
  }

  // Get updated accounts and chainId
  const { accounts, chainId } = payload.params[0];
});

connector.on("disconnect", (error, payload) => {
  if (error) {
    throw error;
  }

  // Delete connector
});

const uri = connector.uri;


$(".wallet-connect-btn").click(function(){
    alert('bru')
    QRCodeModal.open(uri);
})

