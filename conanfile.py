from conans.model import Generator
from conans import ConanFile
from conans.client.generators.qmake import DepsCppQmake

generic_prf_template = """
message("Conan: Using autogenerated {name}.prf")

INCLUDEPATH *= {deps.include_paths}
LIBS *= {deps.lib_paths} {deps.libs}
DEFINES *= {deps.defines}
QMAKE_CXXFLAGS *= {deps.cppflags}
QMAKE_CFLAGS *= {deps.cflags}
QMAKE_LFLAGS *= {deps.exelinkflags}
"""

class qmake_features(Generator):

    @property
    def content(self):
        print("---------------\n\n")
        print(str(self.deps_build_info.deps))
        print(str(self.deps_build_info.include_paths))

        ret = {}

        ret["conan.pri"] = "QMAKEFEATURES *= $$PWD"

        for dep_name, dep_cpp_info in self.deps_build_info.dependencies:
            dep_name =  dep_name.replace("-", "_").replace(".", "_")
            deps = DepsCppQmake(dep_cpp_info)
            ret["{}.prf".format(dep_name)] = generic_prf_template.format(name=dep_name, deps=deps )              

        return ret

    @property
    def filename(self):
        pass

class QMakeFeatureGeneratorPackage(ConanFile):
    name = "QMakeFeatureGen"
    version = "0.1"
    url = "https://github.com/davidtazy/qmake-feature-conan-generator"
    license = "MIT"
    description = "create one prf file per dependency"

    def build(self):
        pass

    def package_info(self):
        self.cpp_info.includedirs = []
        self.cpp_info.libdirs = []
        self.cpp_info.bindirs = []