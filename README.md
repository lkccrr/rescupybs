[![rescupybs](https://img.shields.io/pypi/v/rescupybs?style=flat-square)](https://pypi.org/project/rescupybs/)
[![rescupybs](https://img.shields.io/pypi/pyversions/rescupybs?style=flat-square)](https://pypi.org/project/rescupybs/)
[![rescupybs](https://img.shields.io/pypi/l/rescupybs?style=flat-square)](https://pypi.org/project/rescupybs/)
[![rescupybs](https://img.shields.io/pypi/dm/rescupybs?style=flat-square)](https://pypi.org/project/rescupybs/)
[![rescupybs](https://img.shields.io/pypi/wheel/rescupybs?style=flat-square)](https://pypi.org/project/rescupybs/)
[![rescupybs](https://img.shields.io/github/last-commit/lkccrr/rescupybs?style=flat-square)](https://github.com/lkccrr/rescupybs)
[![rescupybs](https://img.shields.io/github/release-date/lkccrr/rescupybs?style=flat-square)](https://github.com/lkccrr/rescupybs)

### rescupybs

The <b style="color:green;"><i>rescupybs</b></i> is used for band structure plotting or isosurface file exporting from ***rescuplus*** calculation result <b style="color:darkred;"><i>\*.json</b></i> and <b style="color:darkred;"><i>\*.h5</b></i> files. The code will provide two scripts, <b style="color:blue;"><i>rescubs</b></i> for band structure plotting using ***rescuplus*** <b style="color:darkred;"><i>\*.json</b></i> or <b style="color:darkred;"><i>\*.dat</b></i> files, and <b style="color:blue;"><i>rescuiso</b></i> for isosurface file exporting in ***VESTA*** format from <b style="color:darkred;"><i>\*.json</b></i> and <b style="color:darkred;"><i>\*.h5</b></i> files.
***
<b style="color:blue;"><i>rescubs</b></i>
* To execute <b style="color:blue;"><i>rescubs</b></i> <b style="color:red;"><i>\-h</b></i> for the parameters to use.
* Example:
```bash
rescubs -h
rescubs -i nano_bs_out_bs.dat -o band.png -l g m k g
rescubs -b -l g m k g -y -1.2 1.2
```
***
<b style="color:blue;"><i>rescuiso</b></i>
* To execute <b style="color:blue;"><i>rescuiso</b></i> <b style="color:red;"><i>\-h</b></i> for the parameters to use.
* Example:
```bash
rescuiso -h
rescuiso -i nano_wvf_out.json -k 1 4 -b 0 3
```
 
