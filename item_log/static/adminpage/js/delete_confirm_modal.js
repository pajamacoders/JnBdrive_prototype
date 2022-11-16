
$('#delete_modal').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget)
    var id = button.data('bs-id')
    var todo = button.data('bs-todo')
    var type = button.data('bs-type')
    var modal = $(this)
    // name과 todo는 modal-body에 사용 -> body-text에 채워지는 내용
    modal.find('.modal-body').text(type + ' ' + id +'를 삭제하시겠습니까?')
    // id는 url 만들때 사용 -> href의 값으로 채워지는 부분
    modal.find('.modal-footer a').attr('href', todo)

})