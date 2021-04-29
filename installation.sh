# INSTALL THIS FIRST TO USE DJANGO AND W/ POSTGRESQL/POSTGIS

# First update everything
sudo apt -y update
sudo apt -y upgrade

# Create variable names
_GEOS="geos-3.9.1"
_PROJ="proj-8.0.0"
_PROJ_DATA="proj-data-1.5"
_GDAL="gdal-3.2.2"
_POSTGIS="postgis-3.1.2dev"

# Install dependency for: geos
sudo apt-get install -y build-essential 

# Compile/install GEOS
if [ ! -f "$_GEOS.tar.bz2" ]; then
    wget https://download.osgeo.org/geos/$_GEOS.tar.bz2
else
    echo "'$_GEOS.tar.bz2' ALREADY DOWNLOADED"
fi
if [ ! -d "$_GEOS" ]; then
    sudo tar xjf $_GEOS.tar.bz2
    cd $_GEOS
    sudo ./configure
    sudo make
    sudo make install
    cd ..
else
    echo "FOLDER '$_GEOS' ALREADY FOUND"
fi

# Install dependency for: proj & proj-data
sudo apt-get install -y pkg-config sqlite3 libsqlite3-dev libtiff-dev libcurl4-gnutls-dev librtmp-dev

# Compile/install PROJ and PROJ-DATA
if [ ! -f "$_PROJ.tar.gz" ]; then
    wget https://download.osgeo.org/proj/$_PROJ.tar.gz
else
    echo "'$_PROJ.tar.gz' ALREADY DOWNLOADED"
fi
if [ ! -f "$_PROJ_DATA.tar.gz" ]; then
    wget https://download.osgeo.org/proj/$_PROJ_DATA.tar.gz
else
    echo "'$_PROJ_DATA.tar.gz' ALREADY DOWNLOADED"
fi
if [ ! -d "$_PROJ" ] && [ ! -d "$_PROJ/data" ]; then
    sudo tar xzf $_PROJ.tar.gz
    mkdir -p $_PROJ/data # sudo make folder if not exists
    cd $_PROJ/data
    sudo tar xzf ../../$_PROJ_DATA.tar.gz
    cd ..
    sudo ./configure
    sudo make
    sudo make install
    cd ..
else
    echo "FOLDER '$_PROJ' ALREADY FOUND"
fi

# Compile/install GDAL
if [ ! -f "$_GDAL.tar.gz" ]; then
    wget https://download.osgeo.org/gdal/3.2.2/$_GDAL.tar.gz
else
    echo "'$_GDAL.tar.gz' ALREADY DOWNLOADED"
fi
if [ ! -d "$_GDAL" ]; then
    sudo tar xzf $_GDAL.tar.gz
    cd $_GDAL
    sudo ./configure
    sudo make # Go get some coffee, this takes a while.
    sudo make install
    cd ..
else
    echo "FOLDER '$_GDAL' ALREADY FOUND"
fi

# Install dependency for: POSTGIS
sudo apt install -y postgresql-12 postgresql-server-dev-12 postgresql-client-12 libpq-dev libxml2-dev postgis

# Replace a line in postgresql.conf
filename="/etc/postgresql/12/main/postgresql.conf"
sudo sed -i "s/#listen_addresses = 'localhost'/listen_addresses = '*'/" $filename
sudo service postgresql restart

# Compile/install POSTGIS
if [ ! -f "$_POSTGIS.tar.gz" ]; then
    wget http://postgis.net/stuff/$_POSTGIS.tar.gz
else
    echo "'$_POSTGIS.tar.gz' ALREADY DOWNLOADED"
fi
if [ ! -d "$_POSTGIS" ]; then
    sudo tar xvfz $_POSTGIS.tar.gz
    cd $_POSTGIS
    sudo ./configure --without-protobuf
    sudo make
    sudo make install
    cd ..
else
    echo "FOLDER '$_POSTGIS' ALREADY FOUND"
fi

# Install dependency for: django
sudo apt-get install -y python3-django python3-pip
pip3 install -r requirements.txt

# change password hashing of postgresql
filename="/etc/postgresql/12/main/pg_hba.conf"
sudo sed -i "s/local   all             postgres                                peer/local   all             postgres                                trust/" $filename
sudo service postgresql restart
