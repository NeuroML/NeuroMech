import modelspec
from modelspec import field, instance_of, optional
from modelspec.base_types import Base
from typing import List, Optional, Dict, Any
import sys

# Initial ideas for Mujoco integration


@modelspec.define(eq=False)
class MujocoBase(Base):
    """
    Base class for all Mujoco core classes.

    Attributes:
        metadata: Optional metadata field, an arbitrary dictionary of string keys and JSON serializable values.

    """

    metadata: Optional[Dict[str, Any]] = field(
        kw_only=True, default=None, validator=optional(instance_of(dict))
    )


@modelspec.define
class light(MujocoBase):
    """
    Some description...

    Args:
    """

    directional: str = field(default=None, validator=optional(instance_of(str)))
    diffuse: str = field(default=None, validator=optional(instance_of(str)))
    pos: str = field(default=None, validator=optional(instance_of(str)))
    dir: str = field(default=None, validator=optional(instance_of(str)))


@modelspec.define
class geom(MujocoBase):
    """
    Some description...

    Args:
    """

    type: str = field(validator=instance_of(str))
    size: str = field(default=None, validator=optional(instance_of(str)))
    rgba: str = field(default=None, validator=optional(instance_of(str)))


@modelspec.define
class joint(MujocoBase):
    """
    Some description...

    Args:
    """

    type: str = field(validator=instance_of(str))


@modelspec.define
class body(MujocoBase):
    """
    Some description...

    Args:
    """

    pos: str = field(validator=instance_of(str))

    joints: List[joint] = field(factory=list)
    geoms: List[geom] = field(factory=list)


@modelspec.define
class worldbody(MujocoBase):
    """
    Some description...

    Args:
    """

    lights: List[light] = field(factory=list)
    geoms: List[geom] = field(factory=list)
    bodies: List[body] = field(factory=list)


@modelspec.define
class mujoco(MujocoBase):
    """
    Some description...

    Args:
        id: The id of the Mujoco document
    """

    model: str = field(validator=instance_of(str))

    """
    xmlns: str = field(
        validator=instance_of(str), default="http://www.neuromech.org/schema/neuromlech"
    )
    xmlns_xsi: str = field(
        validator=instance_of(str), default="http://www.w3.org/2001/XMLSchema-instance"
    )
    xmlns_loc: str = field(
        validator=instance_of(str),
        default="http://www.neuromech.org/schema/neuromlech https://raw.github.com/NeuroML/NeuroMech/development/NeuroMech_v0.1.xsd",
    )"""

    worldbodies: List[worldbody] = field(factory=list)


if __name__ == "__main__":
    nmc_doc = mujoco(
        model="TestMujoco", metadata={"description": "Testing a Mujoco document"}
    )

    worldbody1 = worldbody()

    worldbody1.lights.append(light(diffuse=".5 .5 .5", pos="0 0 3", dir="0 0 -1"))
    worldbody1.geoms.append(geom(type="plane", size="10 1 0.1", rgba="0 0.9 0 1"))

    nmc_doc.worldbodies.append(worldbody1)

    body0 = body(pos="0 0 1")
    body0.joints.append(joint(type="free"))
    body0.geoms.append(geom(type="box", size="0.1 0.1 0.1", rgba="1 0 0 1"))
    worldbody1.bodies.append(body0)

    body1 = body(pos="0.3 0.3 1.5")
    body1.joints.append(joint(type="free"))
    body1.geoms.append(geom(type="sphere", size="0.15", rgba="1 1 0 1"))
    worldbody1.bodies.append(body1)

    print(nmc_doc)

    nmc_doc.to_json_file("%s.json" % nmc_doc.model)
    nmc_doc.to_xml_file("%s.xml" % nmc_doc.model)
    nmc_doc.to_yaml_file("%s.yaml" % nmc_doc.model)

    print(" >> Full document details in YAML format:\n")
    print(nmc_doc.to_yaml())
    """

    print("Generating documentation...")

    doc_md = nmc_doc.generate_documentation(format="markdown")

    with open("NeuroML2.md", "w") as d:
        d.write(doc_md)

    doc_rst = nmc_doc.generate_documentation(format="rst")

    with open("NeuroML2.rst", "w") as d:
        d.write(doc_rst)

    print("\n  >> Generating specification in dict form...")
    doc_dict = nmc_doc.generate_documentation(format="dict")

    import json
    import yaml

    with open("NeuroML2.specification.json", "w") as d:
        d.write(json.dumps(doc_dict, indent=4))

    print("  >> Generating specification in YAML...\n")

    with open("NeuroML2.specification.yaml", "w") as d:
        yy = yaml.dump(doc_dict, indent=4, sort_keys=False)
        # print(yy)
        d.write(yy)

    from modelspec.utils import load_xml

    new_neuroml = load_xml("hello_world_neuroml.net.nml")
    print(new_neuroml)"""
