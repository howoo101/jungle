//포스팅 박스 열고 닫기 기능
function toggle_postbox(ev) {
            
    let postBoxEl = $("#post-box");
    let postBoxBtnEl = $(ev.target);
    let postBoxBenText = postBoxBtnEl.text();
    console.log("display :" + postBoxEl.css("display"));
    console.log("postBoxBtnText :" + postBoxBenText);
    // block <-> none
    if(postBoxEl.css("display") == "block") {
        postBoxEl.hide();
        postBoxBtnEl.text(postBoxBenText.replace("닫기","열기"));
    }else {
        postBoxBtnEl.text(postBoxBenText.replace("열기","닫기"));
        postBoxEl.show();
    }
    
}