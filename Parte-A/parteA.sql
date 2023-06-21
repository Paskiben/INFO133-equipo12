USE 'parteA';

CREATE TABLE 'prensa' (
  'Pais' varchar(50) NOT NULL,
  'Continente' varchar(50) NOT NULL,
  'Region' varchar(50) NOT NULL,
  'Ciudad' varchar(50) NOT NULL,
  'Nombre_prensa' varchar(50) NOT NULL,
  'Tipo_cobertura' varchar(50) NOT NULL,
  'id_prensa' int(11) NOT NULL,
  'year_fundation' int(11) NOT NULL,
  'url_principal' varchar(50) NOT NULL,
  PRIMARY KEY ('id_prensa')
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE 'fundadores' (
  'Nombre_fundadores' varchar(50) NOT NULL,
  'id_fundadores' int(11) NOT NULL,
  'id_prensa' varchar(50) NOT NULL,
  PRIMARY KEY ('id_fundadores'),
  FOREIGN KEY ('id_prensa') REFERENCES 'prensa' ('id_prensa')
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE 'noticia' (
  'xpath_titulo' varchar(50) NOT NULL,
  'xpath_contenido' varchar(50) NOT NULL,
  'xpath_fecha' varchar(50) NOT NULL,
  'url_noticia' varchar(50) NOT NULL,
  'id_prensa' varchar(50) NOT NULL,
  PRIMARY KEY ('url_noticia'),
  FOREIGN KEY ('id_prensa') REFERENCES 'prensa' ('id_prensa')
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE 'categoria' (
  'xpath_categoria' varchar(50) NOT NULL,
  'url_categoria' varchar(50) NOT NULL,
  'id_prensa' varchar(50) NOT NULL,
  PRIMARY KEY ('url_categoria') NOT NULL,
  FOREIGN KEY ('id_prensa') REFERENCES 'prensa' ('id_prensa') 
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE 'red_social' (
  'nombre_red_social' varchar(50) NOT NULL,
  'id_red_social' int(11) NOT NULL,
  'seguidores' int(20) NOT NULL,
  'id_prensa' varchar(50) NOT NULL,
  PRIMARY KEY ('id_red_social'),
  FOREIGN KEY ('id_prensa') REFERENCES 'prensa' ('id_prensa') 
) ENGINE=InnoDB DEFAULT CHARSET=latin1;