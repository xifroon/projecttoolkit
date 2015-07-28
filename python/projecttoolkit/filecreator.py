import sys
import os
import os.path as path
import shutil
import logging

# Avoid Enum for compatibility
class FileCreatorHint:
    """Enum guiding automatic file creation

    Element:
    Folder -- folder, created if not exists
    SymLink -- symlink to file or folder
    NewFile -- empty file, created if not exists
    StockFile -- stockfile in specified folder
    AltStockFile -- stockfile with many variant
    """
    # DEPRECATED
    NewFolder, StockFileWithType = range(5, 7)
    Folder, SymLink, NewFile, StockFile, AltStockFile = range(5)

class FileCreator:
    Logger = logging.getLogger('projecttoolkit')
    @classmethod
    def createfile(self, filepath):
        if path.exists(filepath):
            mode = 'w+'
            with open(filepath, mode) as f:
                f.close()

    @classmethod
    def createsymlink(self, targetpath, symlinkpath):
        target_isdir = False
        if path.isdir(targetpath):
            target_isdir = True
        try:
            os.symlink(targetpath, symlinkpath, target_isdir)
        except FileExistsError as err:
            self.Logger.warning('symlink already exists: ' + symlinkpath)
            pass

    @classmethod
    def createfolder(self, dirpath, mode=0o750):
        if not path.exists(dirpath):
            os.makedirs(dirpath)

    @classmethod
    def lazycopy(self, src, dest, copy_function=shutil.copy2):
        '''Copy file, if dest exists, abort

        Arguments:
        src -- file or directory
        dest -- file or directory, if directory, it should be the real target
                not parent directory
        postprocessor_cb -- callback post processor function of copied file (dest)
        '''
        if path.exists(src):
            self.Logger.debug('Copying ' + src + ' (%s) to ' % (not path.exists(src)) + dest + " (%s)" % (not path.isfile(dest)))
            if path.isfile(src):
                # lazy copy once destination file exists
                if (not path.exists(dest)):
                    copy_function(src, dest)
            else:
                self.copytree(src, dest, copy_function)

    @classmethod
    def copytree(self, src, dst, symlinks = False, ignore = None, copy_function=shutil.copy2):
        """Enhanced shutil.copytree()"""
        if not os.path.exists(dst):
            os.makedirs(dst)
            shutil.copystat(src, dst)
        lst = os.listdir(src)
        if ignore:
            excl = ignore(src, lst)
            lst = [x for x in lst if x not in excl]
        for item in lst:
            s = os.path.join(src, item)
            d = os.path.join(dst, item)
            if symlinks and os.path.islink(s):
                if os.path.lexists(d):
                    os.remove(d)
                os.symlink(os.readlink(s), d)
                try:
                    st = os.lstat(s)
                    mode = stat.S_IMODE(st.st_mode)
                    os.lchmod(d, mode)
                except:
                    pass # lchmod not available
            elif os.path.isdir(s):
                self.copytree(s, d, symlinks, ignore)
            else:
                copy_function(s, d)
