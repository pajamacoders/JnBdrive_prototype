$('#qrcodemodal').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget)
    var qrcode_url = button.data('bs-todo')
    var save_name = button.data('bs-save')
    var modal = $(this)
    // get qrcode from server
    modal.find('.modal-title').text(save_name+' 의 QRCode')
    img = document.getElementById('qrcode_image')
    img.setAttribute('src', qrcode_url)
    document.getElementById('save_qrcode').addEventListener('click', function() {
        const link = document.createElement('a');
        link.download = save_name+'.png';
        link.href = img.src;
        link.click();
      });
})