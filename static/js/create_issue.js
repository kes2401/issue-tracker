$('#id_title').focus();

setTimeout(function () {
    const toolbar = $('td.mceToolbar');
    $('td.mceToolbar').parent().parent().prepend(toolbar);
    $('#tinymce').attr('style', 'font-size: 1rem;')
}, 500); // ===== TODO: build a better way of manipulating TinyMCE text editor when after its created in the DOM =====