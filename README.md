###<!---li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                Locations
              </a>
              <div class="dropdown-menu" aria-labelledby="navbarDropdown">
                  {% for location in locations %}
                <a class="dropdown-item" href="{% url 'location' location.id %}">{{location}}</a>
                  {% endfor %}
            </li-->