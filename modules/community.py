import streamlit as st


# --------------------------------------------------
# INIT COMMUNITY STORAGE
# --------------------------------------------------
def init_community():
    if "posts" not in st.session_state:
        st.session_state.posts = []


# --------------------------------------------------
# ADD NEW POST
# --------------------------------------------------
def add_post(author, text):
    post = {
        "author": author,
        "text": text,
        "votes": 0
    }
    st.session_state.posts.append(post)


# --------------------------------------------------
# UPVOTE
# --------------------------------------------------
def upvote_post(index):
    st.session_state.posts[index]["votes"] += 1


# --------------------------------------------------
# GET SORTED POSTS
# --------------------------------------------------
def get_posts_sorted():
    return sorted(
        st.session_state.posts,
        key=lambda x: x["votes"],
        reverse=True
    )


# --------------------------------------------------
# MAIN COMMUNITY UI
# --------------------------------------------------
def community_ui():
    init_community()

    st.subheader("🌍 Community Wisdom")

    # ---------------- ADD POST ----------------
    st.write("Share your advice with others:")

    new_post = st.text_area("Your thought")

    if st.button("Post"):
        if new_post.strip():
            add_post(st.session_state.user, new_post)
            st.success("Your wisdom has been shared 🌱")
            st.rerun()
        else:
            st.warning("Please write something.")

    st.divider()

    # ---------------- SHOW POSTS ----------------
    st.subheader("🔥 Top Ideas")

    posts = get_posts_sorted()

    if not posts:
        st.info("No posts yet. Be the first to share.")

    for i, post in enumerate(posts):
        col1, col2 = st.columns([5, 1])

        with col1:
            st.write(f"**{post['author']}**: {post['text']}")

        with col2:
            if st.button(f"👍 {post['votes']}", key=f"vote_{i}"):
                upvote_post(i)
                st.rerun()
