import jinja2
import utilities


def foo():
    return "foo() called"


def test_template_render():
    template1 = jinja2.Template("{{ 10 + 3 }}")

    assert "13" == template1.render()


def test_template_render_param():
    template1 = jinja2.Template("{{ var }}")

    assert "12" == template1.render(var=12)


def test_template_render_function():
    template1 = jinja2.Template("{{ foo() }}")

    assert foo() == template1.render(foo=foo)


def test_loader():
    templates_folder = str(utilities.get_data_path().joinpath("templates"))
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(templates_folder))
    template = env.get_template("my_template.html")

    assert "html" in template.render()
