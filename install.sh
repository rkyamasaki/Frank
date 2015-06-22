#Check if python is already installed
#if is not installed then, it will be installed
if which python2.7 >/dev/null; then
	echo "Python 2.7 is already installed."
else
	echo "Installing Python 2.7"
	sudo add-apt-repository ppa:fkrull/deadsnakes
	sudo apt-get update
	sudo apt-get install python2.7
fi

echo "Installing python-dev"
sudo apt-get install python-dev

echo "Installing python-psutil"
sudo apt-get install python-psutil


echo "           ,,====-------------------====,,          "
echo "         ###                             ###        "
echo "        ###   -|-                         ###       "
echo "       ###    -|-                          ###      "
echo "       ###    -|-                          ###      "
echo "       ####                               ####      "
echo "       ###    ________________________     ###      "
echo "       ### ////////////     \\\\\\\\\\\\\  ###      "
echo "       ###///      \'/       \`/       \\\ ###      "
echo "       ###'':=======/         \========:`` ###      "
echo "     /\##'''  ___  /           \  ___   ````##/\    "
echo "    /  \#         ( O _______ O )           #/  \   "
echo "   |                                             |  "
echo "   |                    | |                      |  "
echo "    \                   | |                     /   "
echo "     \___|          ,=========,            |___/    "
echo "         |\     ,,//'''''''''''\\,,       /|        "
echo "         | |          _______            | |        "
echo "         | \         '       '          /  |        "
echo "         |  \                          /   |        "
echo "   __    |   \                        /    |    __  "
echo "  |  |---|    \,____________________,'     |---|  | "
echo "  |__|---|                                 |---|__| "
echo "         |                                 |        "
echo "         |      INSTALLATION COMPLETE      |        " 

