jQuery("#js-drawer-icon").on("click", function (e) {
    e.preventDefault();
    jQuery("#js-drawer-icon").toggleClass("is-checked");
    jQuery("#js-drawer-content").toggleClass("is-checked");
});

jQuery('a[href^="#"]').on("click", function(e){
    e.preventDefault(); // デフォルトの動作をキャンセルする
    const speed = 800;
    const id = jQuery(this).attr("href"); // "this" の前にjQueryを付け足す必要があります
    const target = jQuery(id === "#" ? "html" : id); // id === "#" で比較する必要があります
    if (target.length) { // ターゲットが存在するか確認する
        const position = target.offset().top; // jQuery(target) を使う必要はありません
        jQuery("html, body").animate(
            {
                scrollTop: position,
            },
            speed,
            "swing" // "swing" または "linear" を使います
        );
    }
});


jQuery(window).on("scroll", function(){
    if ( 200 < jQuery(window).scrollTop()){
      jQuery("#js-pagetop").addClass("is-show");
    }else{
      jQuery("#js-pagetop").removeClass("is-show");
  
    }
  });

const intersectionObserver = new IntersectionObserver(function(entries){
entries.forEach(function(entry){
    if (entry.isIntersecting){
    entry.target.classList.add("is-in-view");
    }else{
    entry.target.classList.remove("is-in-view");
    }
});
});

const inViewItems = document.querySelectorAll(".js-in-view");
inViewItems.forEach(function(inViewItem){
intersectionObserver.observe(inViewItem)
});

document.addEventListener("DOMContentLoaded", function() {
    var showMoreButton = document.getElementById("showMoreButton");
    var hiddenContainers = document.querySelectorAll(".work__container.hidden");
    
    showMoreButton.addEventListener("click", function() {
      hiddenContainers.forEach(function(container) {
        container.classList.toggle("hidden");
      });
      showMoreButton.style.display = "none"; // ボタンを非表示にする
    });
  });
  

  let winHeight,winScroll,scrollPos;
$(window).on('load scroll',function(){
	winScroll = $(window).scrollTop();
	winHeight = $(window).height();
	scrollPos = winHeight * 0.9 + winScroll;
	$(".slidein").each(function(){
		if($(this).offset().top <= scrollPos){
			$(this).addClass("show");
		}else{
			$(this).removeClass("show");
		}
	});
});

$(document).ready(function() {
  $(window).scroll(function() {
    var header = $("header");
    var scrollY = $(window).scrollTop();
    
    if (scrollY >= 700) {
      header.css("background-color", "#fff"); // 背景色を黒色に変更
    } else {
      header.css("background-color", "rgba(0,0,0,0)"); // 背景色を赤色に変更
    }
  });
});

$(document).ready(function() {
  var workContainers = $('.work__container');
  var showAllBtn = $('.show-all-btn');
  var initiallyVisibleCount = 3;

  function showAllWorks() {
    workContainers.slice(initiallyVisibleCount).css('display', 'block');
    showAllBtn.hide();
  }

  // Initially display only the first 3 works
  workContainers.slice(0, initiallyVisibleCount).css('display', 'block');

  // Show the "Show All" button if there are more than 3 works
  if (workContainers.length > initiallyVisibleCount) {
    showAllBtn.show();
  }

  showAllBtn.on('click', showAllWorks);
});


// jQuery function to scroll to the top of the page
function scrollToTop() {
  $('html, body').animate({ scrollTop: 0 }, 'slow');
  return false; // Important: Prevent default behavior of the anchor link
}

// Show or hide the scrollToTop button based on scroll position
$(window).scroll(function() {
  toggleScrollToTopButton($(window).scrollTop());
});

function toggleScrollToTopButton(scrollPosition) {
  var scrollToTopBtn = $('#js-pagetop');
  if (scrollPosition > 20) {
    scrollToTopBtn.fadeIn();
  } else {
    scrollToTopBtn.fadeOut();
  }
}