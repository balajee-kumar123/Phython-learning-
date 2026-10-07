# file_manager_app.py
import streamlit as st
from pathlib import Path
import os
import datetime

# ---------- Page config ----------
st.set_page_config(
    page_title="File Manager — CRUD",
    page_icon="📁",
    layout="centered",
    initial_sidebar_state="expanded",
)

# ---------- Styling ----------
st.markdown(
    """
    <style>
    .stApp { background: linear-gradient(180deg,#f7f9fc,#ffffff); }
    .card { padding: 18px; border-radius: 12px; background: #ffffff; box-shadow: 0 6px 18px rgba(0,0,0,0.06); }
    .muted { color: #6b7280; font-size: 0.95rem; }
    .small { font-size: 0.9rem; color:#374151; }
    .file-meta { color:#6b7280; font-size:0.85rem; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------- Helper functions ----------
BASE_DIR = Path.cwd()

def list_files(folder: Path = BASE_DIR, pattern: str = "*"):
    return sorted([p for p in folder.glob(pattern) if p.is_file()])

def read_file(path: Path):
    try:
        return path.read_text(encoding="utf-8")
    except Exception as e:
        st.error(f"Could not read file: {e}")
        return ""

def write_file(path: Path, content: str, mode: str = "w"):
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, mode, encoding="utf-8") as f:
            f.write(content)
        return True, None
    except Exception as e:
        return False, str(e)

def delete_file(path: Path):
    try:
        path.unlink()
        return True, None
    except Exception as e:
        return False, str(e)

# ---------- Sidebar (navigation) ----------
st.sidebar.title("File Manager")
st.sidebar.markdown("A simple CRUD UI built with **Streamlit**")
action = st.sidebar.radio("Choose action", ["Create", "Read", "Update", "Delete", "Browse"])

st.sidebar.divider()
st.sidebar.markdown("**Working directory**")
st.sidebar.write(f"`{BASE_DIR}`")
st.sidebar.markdown("---")
st.sidebar.markdown("Tip: Use the Browse tab to filter and manage files.")

# ---------- Main UI ----------
st.title("📁 File Manager — Create · Read · Update · Delete")
st.markdown("A clean UI for file handling. Use responsibly — this app works with files in the current working directory.")

st.markdown("")  # spacing

# ---------- Browse (file list + quick actions) ----------
if action == "Browse":
    st.header("Browse files")
    pattern = st.text_input("Filename pattern (glob)", value="*.*", help="Examples: *.txt, *.py, report_*.md")
    files = list_files(BASE_DIR, pattern)
    st.write(f"**{len(files)}** file(s) found")
    for p in files:
        with st.container():
            st.markdown(f"<div class='card'>", unsafe_allow_html=True)
            cols = st.columns([0.7, 0.15, 0.15])
            cols[0].markdown(f"**{p.name}**  \n<span class='file-meta'>Size: {p.stat().st_size} bytes · Modified: {datetime.datetime.fromtimestamp(p.stat().st_mtime).strftime('%Y-%m-%d %H:%M:%S')}</span>", unsafe_allow_html=True)
            if cols[1].button("Preview", key=f"preview_{p}", help="Open preview"):
                st.session_state["_preview_file"] = str(p)
            if cols[2].button("Delete", key=f"del_{p}", help="Delete file"):
                st.session_state["_delete_target"] = str(p)
            st.markdown("</div>", unsafe_allow_html=True)

    # Preview modal-like area
    if st.session_state.get("_preview_file"):
        preview_path = Path(st.session_state["_preview_file"])
        st.markdown("---")
        st.subheader(f"Preview — {preview_path.name}")
        content = read_file(preview_path)
        st.code(content, language="text")
        st.download_button("Download file", data=content, file_name=preview_path.name)

    # Delete confirmation
    if st.session_state.get("_delete_target"):
        target = Path(st.session_state["_delete_target"])
        st.warning(f"Are you sure you want to delete **{target.name}**?")
        c1, c2 = st.columns(2)
        if c1.button("Yes, delete"):
            ok, err = delete_file(target)
            if ok:
                st.success(f"Deleted {target.name}")
                st.session_state.pop("_delete_target", None)
                st.session_state.pop("_preview_file", None)
            else:
                st.error(f"Error deleting file: {err}")
        if c2.button("Cancel"):
            st.session_state.pop("_delete_target", None)

# ---------- Create ----------
if action == "Create":
    st.header("Create a new file")
    with st.form("create_form"):
        fname = st.text_input("Filename (with extension)", placeholder="hello.txt")
        use_upload = st.checkbox("Create from uploaded file", value=False)
        uploaded = None
        if use_upload:
            uploaded = st.file_uploader("Upload a file to save as", type=None)
        content = st.text_area("File content", height=200, placeholder="Write your content here...")
        overwrite = st.checkbox("Overwrite if file exists", value=False)
        submitted = st.form_submit_button("Create file")
    if submitted:
        if not fname:
            st.error("Please provide a filename.")
        else:
            path = BASE_DIR / fname
            if path.exists() and not overwrite:
                st.error("File already exists. Check 'Overwrite if file exists' to replace it.")
            else:
                if use_upload and uploaded is not None:
                    data = uploaded.getvalue().decode("utf-8", errors="ignore")
                else:
                    data = content
                ok, err = write_file(path, data, mode="w")
                if ok:
                    st.success(f"File **{fname}** created successfully.")
                    st.balloons()
                    st.download_button("Download created file", data=data, file_name=fname)
                else:
                    st.error(f"Failed to create file: {err}")

# ---------- Read ----------
if action == "Read":
    st.header("Read a file")
    files = list_files(BASE_DIR, "*.*")
    file_names = [p.name for p in files]
    selected = st.selectbox("Select a file to read", [""] + file_names)
    if selected:
        path = BASE_DIR / selected
        st.markdown(f"**{selected}**")
        try:
            content = read_file(path)
            st.code(content, language="text")
            st.download_button("Download file", data=content, file_name=selected)
        except Exception as e:
            st.error(f"Error: {e}")

# ---------- Update ----------
if action == "Update":
    st.header("Update a file")
    files = list_files(BASE_DIR, "*.*")
    file_names = [p.name for p in files]
    selected = st.selectbox("Select a file to update", [""] + file_names)
    if selected:
        path = BASE_DIR / selected
        original = read_file(path)
        st.markdown(f"**Editing {selected}**")
        mode = st.radio("Update mode", ["Append", "Overwrite"], index=0)
        new_text = st.text_area("Enter text to append/overwrite", value="", height=200)
        if st.button("Apply update"):
            if not new_text:
                st.warning("No text entered. Nothing to do.")
            else:
                write_mode = "a" if mode == "Append" else "w"
                ok, err = write_file(path, new_text, mode=write_mode)
                if ok:
                    st.success(f"File {selected} updated ({mode}).")
                    st.download_button("Download updated file", data=read_file(path), file_name=selected)
                else:
                    st.error(f"Update failed: {err}")

# ---------- Delete ----------
if action == "Delete":
    st.header("Delete a file")
    files = list_files(BASE_DIR, "*.*")
    file_names = [p.name for p in files]
    selected = st.selectbox("Select a file to delete", [""] + file_names)
    if selected:
        path = BASE_DIR / selected
        st.markdown(f"**{selected}**")
        st.write(f"Size: {path.stat().st_size} bytes · Modified: {datetime.datetime.fromtimestamp(path.stat().st_mtime).strftime('%Y-%m-%d %H:%M:%S')}")
        if st.button("Delete file"):
            ok, err = delete_file(path)
            if ok:
                st.success(f"{selected} deleted.")
            else:
                st.error(f"Could not delete file: {err}")

# ---------- Footer ----------
st.markdown("---")
st.markdown("Built with ❤️ using **Streamlit** · Keep files in the app folder for safety.")
