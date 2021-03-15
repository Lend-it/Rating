\c ratelenditdb_dev

INSERT INTO public.rate
  (rateid,stars,review,report,reviewed,reviewer, requestid)
VALUES
  ('8ec75836-5b11-4fd4-8391-9f6719b282f7',5.0,'Pessoa de extrema confiança! Pegou meu livro e devolveu em perfeito estado no prazo.',false,'rogerio@email.com','lucas@email.com','8d27b6c1-ac8a-4f29-97b0-96cef6938267'),
  ('6cf86d56-fafe-444a-bf7d-b4212597f635',4.9,'',false,'esio@email.com','rogerio@email.com','fce61c6d-1cb0-488c-a2fa-6a90fdbe192d'),
  ('dd6fd6fb-f3ec-4c47-bf4c-99a891af6ee4',3.0,'Devolveu meu secador sem defeitos, mas me entregou com 1 dia de atraso.',false,'youssef@email.com','rogerio@emal.com','1c1ad4cd-ce57-485d-bc6c-72941386bc99'),
  ('6e10dffb-cae6-4c87-9bc0-35868a44624b',1.0,'Devolveu sem ter lavado! Nunca mais empresto nada para esse cara!! É inacreditável como em pleno século XXI um cara desses faz uma coisa dessas!!!! ',true,'lucas@email.com','youssef@email.com','63f9ea52-c81e-4279-91f4-c5d61d2e9c31'),
  ('b5b05147-3298-4dc6-bfc4-4613271e7080',3.2,'Não tive problemas com relação a devolução do meu PS3, mas ele é muito mal humorado e sem educação.. não me disse nem obrigado!',false,'youssef@email.com','esio@email.com','9406ab9c-a0e2-4ec3-8779-a45ec7788f7c');