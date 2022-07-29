$(function() {

  $('input[type="checkbox"]').change(checkboxChanged);

  function checkboxChanged() {
    var $this = $(this),
        checked = $this.prop("checked"),
        container = $this.parent(),
        siblings = container.siblings();

    container.find('input[type="checkbox"]')
    .prop({
        indeterminate: false,
        checked: checked
    })
    .siblings('label')
    .removeClass('custom-checked custom-unchecked custom-indeterminate')
    .addClass(checked ? 'custom-checked' : 'custom-unchecked');

    checkSiblings(container, checked);
  }

  function checkSiblings($el, checked) {
    var parent = $el.parent().parent(),
        all = true,
        indeterminate = false;

    $el.siblings().each(function() {
      return all = ($(this).children('input[type="checkbox"]').prop("checked") === checked);
    });

    if (all && checked) {
      parent.children('input[type="checkbox"]')
      .prop({
          indeterminate: false,
          checked: checked
      })
      .siblings('label')
      .removeClass('custom-checked custom-unchecked custom-indeterminate')
      .addClass(checked ? 'custom-checked' : 'custom-unchecked');

      checkSiblings(parent, checked);
    } 
    else if (all && !checked) {
      indeterminate = parent.find('input[type="checkbox"]:checked').length > 0;
      parent.children('input[type="checkbox"]')
      .prop("checked", checked)
      .prop("indeterminate", indeterminate)
      .siblings('label')
      .removeClass('custom-checked custom-unchecked custom-indeterminate')
      .addClass(indeterminate ? 'custom-indeterminate' : (checked ? 'custom-checked' : 'custom-unchecked'));

      checkSiblings(parent, checked);
    } 
    else {
      $el.parents("li").children('input[type="checkbox"]')
      .prop({
          indeterminate: true,
          checked: false
      })
      .siblings('label')
      .removeClass('custom-checked custom-unchecked custom-indeterminate')
      .addClass('custom-indeterminate');
    }
  }

    $('#create').click(function(){
	console.log("this is a click")
	var myCheckboxes = [];
	$(':checkbox:checked').each(function(i){
	    myCheckboxes.push($(this).val()); // changed this line
	});
	console.log(myCheckboxes)
	$.ajax({
    	    type:'POST',
    	    url:'/cgi-bin/checkboxes.py',
    	    data:{mycheckb: myCheckboxes},
	    success: function(response) {
		    alert(response);
		},
            error: function(response) {
		alert(response);
            } 
    	});
    });


    //       val[i] = $(this).val();
    //     });
    // 	console.log(val);
    // 	var textFile = null,
    // 	makeTextFile = function (text) {
    // 	    var data = new Blob([text], {type: 'text/plain'});

    // 	   If we are replacing a previously generated file we need to
    // 	   manually revoke the object URL to avoid memory leaks.
    // 	    if (textFile !== null) {
    // 		window.URL.revokeObjectURL(textFile);
    // 	    }

    // 	    textFile = window.URL.createObjectURL(data);
    // 	    console.log("I am in text file");
    // 	    return textFile;
    // 	};
    // 	var link = document.getElementById('downloadlink');
    // 	link.href = makeTextFile(val);
    // 	link.style.display = 'block';
   
    // })										
   

    $('#config_page').click(function() {
	location.href='link.html';
    });
    $('#get_platform_info').click(function(e) {
        e.preventDefault();
	//	 var ip = document.getElementById('ip').value
	//	 var pwd = document.getElementById('pwd').value
	
	var ip = sessionStorage.getItem('ip')
	var pwd = sessionStorage.getItem('pwd')
        $.ajax({
            type: 'POST',
            url: "/cgi-bin/test.py",
            data:{pwd:$('form').find('#pwd').val(), ip: $('form').find('#ip').val()},
            success: function(response) {
		alert(response);
            },
            error: function(response) {
		alert(response);
            }
	}).done(function(data){
	    $('#monitor_data').append(data)
	})
    });
    $('#run').click(function(e) {
        e.preventDefault();
        $.ajax({
            type: 'POST',
            url: "/cgi-bin/open.py",
            data:{pwd:$('form').find('#pwd').val(), ip: $('form').find('#ip').val()},
            success: function(response) {
		alert(response);
            },
            error: function(response) {
		alert(response);
            }
	}).done(function(data){
	    $('#results_file').append(data)
	})   
    });
    
	// $('#send').click(function(e) {
    //     e.preventDefault();
    //      $.ajax({
    //         type: 'POST',
    //         url: "/cgi-bin/mail.py",
    //         data:{id:$('form').find('#id').val()},
    //     success: function(response) {
    //         alert(response);
    //     }
    //     error: function(response) {
    //         alert(response);
    //     }
    // 	})
    // });

    $('#save').click(function() {
	$.ajax({
	    type: 'POST',
	    url: "/cgi-bin/info.txt",
	    data:{pwd:$('form').find('#pwd').val(), ip: $('form').find('#ip').val()},
	});
    });
});
