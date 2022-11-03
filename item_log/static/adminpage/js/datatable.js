$(document).ready(function () {
    var table = $('#example').DataTable({
        order: [[0, 'asc']],
        columnDefs: [
            {
                target: 2,
                visible: true,
                searchable: false,
            },
        ],
        rowReorder: {
            selector: 'td:nth-child(2)'
        },
        responsive: true
    });
});