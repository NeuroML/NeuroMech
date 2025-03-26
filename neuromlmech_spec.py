import modelspec
from modelspec import field, instance_of, optional
from modelspec.base_types import Base
from typing import List
import sys

# Initial ideas for NeuroMech specification


@modelspec.define
class point3d(Base):
    """
    Some description...

    Args:
    """

    x: float = field(validator=instance_of(float))
    y: float = field(validator=instance_of(float))
    z: float = field(validator=instance_of(float))


@modelspec.define
class muscle(Base):
    """
    Some description...

    Args:
        target: the target of the input
        input: the input, e.g. pulseGenerator
    """

    id: str = field(validator=instance_of(str))
    start: point3d = field(default=None, validator=optional(instance_of(point3d)))
    end: point3d = field(default=None, validator=optional(instance_of(point3d)))


@modelspec.define
class body(Base):
    """
    Some description...

    Args:
        id: The id of the body
        component: the component to use in the population
        size: the size of the population
    """

    id: str = field(validator=instance_of(str))

    muscles: List[muscle] = field(factory=list)


@modelspec.define
class neuromech(Base):
    """
    Some description...

    Args:
        id: The id of the NeuroMech document
    """

    id: str = field(validator=instance_of(str))

    xmlns: str = field(
        validator=instance_of(str), default="http://www.neuromech.org/schema/neuromlech"
    )
    xmlns_xsi: str = field(
        validator=instance_of(str), default="http://www.w3.org/2001/XMLSchema-instance"
    )
    xmlns_loc: str = field(
        validator=instance_of(str),
        default="http://www.neuromech.org/schema/neuromlech https://raw.github.com/NeuroML/NeuroMech/development/NeuroMech_v0.1.xsd",
    )

    bodies: List[body] = field(factory=list)


if __name__ == "__main__":
    nmc_doc = neuromech(id="TestNeuroMech")

    p1 = point3d(0.0, 0.0, 0.0)
    p2 = point3d(10.0, 10.0, 0.0)

    muscle1 = muscle("bicep", p1, p2)
    body1 = body("forelimb")
    body1.muscles.append(muscle1)

    nmc_doc.bodies.append(body1)

    print(nmc_doc)

    nmc_doc.to_json_file("%s.json" % nmc_doc.id)
    nmc_doc.to_xml_file("%s.xml" % nmc_doc.id)
    nmc_doc.to_yaml_file("%s.yaml" % nmc_doc.id)
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
