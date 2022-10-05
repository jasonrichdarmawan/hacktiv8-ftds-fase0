
$ brew install pandoc
$ brew cask install basictex
$ eval "$(/usr/libexec/path_helper)"
sudo tlmgr update --self
sudo tlmgr install adjustbox
sudo tlmgr install tcolorbox
sudo tlmgr install collectbox
sudo tlmgr install ucs
sudo tlmgr install environ
sudo tlmgr install titling
sudo tlmgr install enumitem
sudo tlmgr install rsfs
$ jupyter nbconvert --execute --to pdf main.ipynb