#!/bin/csh
# Concatenate sfc and atm files.
if ( ! -e new.nc ) then
    ncrcat /glade/scratch/mwong/dave/ufs-mrw/2020070818/sfcf*.nc sfc.nc
    ncrcat /glade/scratch/mwong/dave/ufs-mrw/2020070818/atmf*.nc atm.nc
    cp sfc.nc new.nc
    ncks -A atm.nc new.nc
endif
# change units attribute to K/s 
set cmd = ncatted
foreach var_nm (cnvgwd deepcnv lw microphy nophys orogwd pbl phys rdamp shlwcnv sw)
    set cmd="$cmd -a units,dt3dt_$var_nm,m,c,K/s"
end
$cmd -O new.nc new.nc
