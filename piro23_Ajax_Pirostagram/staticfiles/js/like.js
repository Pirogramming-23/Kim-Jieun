const onClickLike = async(id) =>{
    const url = "/like_ajax/";
    const res = await fetch(url, { 
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({id: id}),
    });
    const data = await res.json();
    const { id: postId, likes: updatedLikes } = data;

    likeHandleResponse(postId, updatedLikes);
}

const likeHandleResponse = (id, updatedLikes) => {
    const likesCountElement = document.getElementById(`likes-count-${id}`);
    likesCountElement.innerHTML = `${updatedLikes}`;
}