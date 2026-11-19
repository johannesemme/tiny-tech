"""Step 1: tg init."""


def test_init_succeeds(tg):
    result = tg("init")
    assert result.returncode == 0, result.stderr


def test_init_creates_the_warehouse_for_boxes(tg, tmp_path):
    tg("init")
    assert (tmp_path / ".tg" / "objects").is_dir()


def test_init_creates_the_folder_for_branch_notes(tg, tmp_path):
    tg("init")
    assert (tmp_path / ".tg" / "refs" / "heads").is_dir()


def test_head_says_we_are_on_main(tg, tmp_path):
    tg("init")
    assert (tmp_path / ".tg" / "HEAD").read_text() == "ref: refs/heads/main\n"


def test_real_git_recognizes_the_repository(tg, git):
    tg("init")
    result = git("symbolic-ref", "HEAD")
    assert result.returncode == 0, result.stderr
    assert result.stdout.strip() == "refs/heads/main"


def test_init_twice_refuses_and_keeps_existing_repository(tg, tmp_path):
    tg("init")
    marker = tmp_path / ".tg" / "objects" / "keep-me"
    marker.write_text("pretend this is a saved box")

    result = tg("init")

    assert result.returncode != 0
    assert "already" in result.stderr.lower()
    assert marker.exists()
