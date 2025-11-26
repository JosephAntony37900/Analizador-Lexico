graph TD
    q0((Inicio)) -->|s| q_s
    q0 -->|m| q_m
    q0 -->|r| q_r
    q0 -->|h| q_h
    q0 -->|i| q_i
    q0 -->|f| q_f

    %% Rama SI / SINO
    q_s -->|i| q_si(((KW_SI)))
    q_si -->|n| q_sin
    q_sin -->|o| q_sino(((KW_SINO)))

    %% Rama FIN
    q_f -->|i| q_fi
    q_fi -->|n| q_fin(((KW_FIN)))

    %% Rama MIENTRAS
    q_m -->|i| q_mi
    q_mi -->|e| q_mie
    q_mie -->|n| q_mien
    q_mien -->|t| q_mient
    q_mient -->|r| q_mientr
    q_mientr -->|a| q_mientra
    q_mientra -->|s| q_mientras(((KW_MIENTRAS)))

    %% Rama REPITE
    q_r -->|e| q_re
    q_re -->|p| q_rep
    q_rep -->|i| q_repi
    q_repi -->|t| q_repit
    q_repit -->|e| q_repite(((KW_REPITE)))

    %% Rama HASTA
    q_h -->|a| q_ha
    q_ha -->|s| q_has
    q_has -->|t| q_hast
    q_hast -->|a| q_hasta(((KW_HASTA)))

    %% Rama INICIO / IMPRIMIR
    q_i -->|n| q_in
    q_in -->|i| q_ini
    q_ini -->|c| q_inic
    q_inic -->|i| q_inici
    q_inici -->|o| q_inicio(((KW_INICIO)))

    q_i -->|m| q_im
    q_im -->|p| q_imp
    q_imp -->|r| q_impr
    q_impr -->|i| q_impri
    q_impri -->|m| q_imprim
    q_imprim -->|i| q_imprimi
    q_imprimi -->|r| q_imprimir(((KW_IMPRIMIR)))