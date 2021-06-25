# add THIS FIRST TO USE DJANGO AND W/ POSTGRESQL/POSTGIS

# First update everything
apk update
apk upgrade

# Create variable names
_GEOS="geos-3.9.1"
_PROJ="proj-8.0.0"
_PROJ_DATA="proj-data-1.5"
_GDAL="gdal-3.2.2"
_POSTGIS="postgis-3.1.2dev"

# add dependency for: geos
apk add build-essential 

# Compile/add GEOS
if [ ! -f "$_GEOS.tar.bz2" ]; then
    wget https://download.osgeo.org/geos/$_GEOS.tar.bz2
else
    echo "'$_GEOS.tar.bz2' ALREADY DOWNLOADED"
fi
if [ ! -d "$_GEOS" ]; then
    tar xjf $_GEOS.tar.bz2
    cd $_GEOS
    ./configure
    make
    make add
    cd ..
else
    echo "FOLDER '$_GEOS' ALREADY FOUND"
fi

# add dependency for: proj & proj-data
apk add pkg-config sqlite3 libsqlite3-dev libtiff-dev libcurl4-gnutls-dev librtmp-dev

# Compile/add PROJ and PROJ-DATA
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
    tar xzf $_PROJ.tar.gz
    mkdir -p $_PROJ/data # make folder if not exists
    cd $_PROJ/data
    tar xzf ../../$_PROJ_DATA.tar.gz
    cd ..
    ./configure
    make
    make add
    cd ..
else
    echo "FOLDER '$_PROJ' ALREADY FOUND"
fi

# Compile/add GDAL
if [ ! -f "$_GDAL.tar.gz" ]; then
    wget https://download.osgeo.org/gdal/3.2.2/$_GDAL.tar.gz
else
    echo "'$_GDAL.tar.gz' ALREADY DOWNLOADED"
fi
if [ ! -d "$_GDAL" ]; then
    tar xzf $_GDAL.tar.gz
    cd $_GDAL
    ./configure
    make # Go get some coffee, this takes a while.
    make add
    cd ..
else
    echo "FOLDER '$_GDAL' ALREADY FOUND"
fi

# add dependency for: POSTGIS
apk add postgresql-12 postgresql-server-dev-12 postgresql-client-12 libpq-dev libxml2-dev postgis

# Replace a line in postgresql.conf
filename="/etc/postgresql/12/main/postgresql.conf"
sed -i "s/#listen_addresses = 'localhost'/listen_addresses = '*'/" $filename
service postgresql restart

# Compile/add POSTGIS
if [ ! -f "$_POSTGIS.tar.gz" ]; then
    wget http://postgis.net/stuff/$_POSTGIS.tar.gz
else
    echo "'$_POSTGIS.tar.gz' ALREADY DOWNLOADED"
fi
if [ ! -d "$_POSTGIS" ]; then
    tar xvfz $_POSTGIS.tar.gz
    cd $_POSTGIS
    ./configure --without-protobuf
    make
    make add
    cd ..
else
    echo "FOLDER '$_POSTGIS' ALREADY FOUND"
fi

# add dependency for: django
apk add python3-django python3-pip
pip3 add -r requirements.txt

# change password hashing of postgresql
filename="/etc/postgresql/12/main/pg_hba.conf"
sed -i "s/local   all             postgres                                peer/local   all             postgres                                trust/" $filename
service postgresql restart
