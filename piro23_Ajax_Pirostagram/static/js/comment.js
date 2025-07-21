const onClickComment = async (form) => {
    const postId = form.dataset.postId;
    const contentInput = form.querySelector('.comment-input');
    const commentContent = contentInput.value.trim();

    if (!commentContent) return;

    const url = "/add_comment/";
    
    const res = await fetch(url, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                post_id: postId,
                content: commentContent
            }),
        });

        const newCommentData = await res.json();
        
        contentInput.value = '';

        handleCommentResponse(postId, newCommentData);
};

const handleCommentResponse = (postId, comment) => {
    let commentList = document.getElementById('comment-list');
    if (!commentList) {
        commentList = document.getElementById(`comment-list-${postId}`);
    }
    if (commentList) {
        const newCommentElement = document.createElement('div');
        newCommentElement.className = 'comment-obj';

        newCommentElement.innerHTML = `
            <div class="comment-area">
                <a href="#">${comment.author_username}</a>
                <div>${comment.content}</div>
            </div>
            <div class="comment-inter">
                방금 전
                <a href="#">답글 달기</a>
            </div>
        `;
        commentList.appendChild(newCommentElement);
    }

    const countSpan = document.getElementById(`comment-count-${postId}`);
    if (countSpan) {
        countSpan.textContent = parseInt(countSpan.textContent) + 1;
    }
};


document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.comment-form').forEach(form => {
        form.addEventListener('submit', (event) => {
            event.preventDefault();
            onClickComment(form);
        });
    });
});