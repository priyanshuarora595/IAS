-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 29, 2022 at 08:03 AM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.1.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ias`
--

-- --------------------------------------------------------

--
-- Table structure for table `accounts_logininfo`
--

CREATE TABLE `accounts_logininfo` (
  `id` bigint(20) NOT NULL,
  `genre` varchar(200) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `accounts_logininfo`
--

INSERT INTO `accounts_logininfo` (`id`, `genre`, `user_id`) VALUES
(4, '', 6);

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add login info', 7, 'add_logininfo'),
(26, 'Can change login info', 7, 'change_logininfo'),
(27, 'Can delete login info', 7, 'delete_logininfo'),
(28, 'Can view login info', 7, 'view_logininfo'),
(29, 'Can add items', 8, 'add_items'),
(30, 'Can change items', 8, 'change_items'),
(31, 'Can delete items', 8, 'delete_items'),
(32, 'Can view items', 8, 'view_items');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(5, 'pbkdf2_sha256$260000$Va0sdR40E9lNuu1cCwFxUM$5D5vzRkDL2vVndp2EyvsNm/01B0hHIbGUlfB2GiuEvw=', '2022-07-27 11:19:25.408080', 1, 'admin', '', '', '', 1, 1, '2022-07-25 07:16:53.153173'),
(6, 'pbkdf2_sha256$260000$u5pt1o54aaXANIXJQZtHGI$DnxSisX9iTf938m/UzTnZ2y572isWg2iiOjZjKupE3Q=', '2022-07-29 05:31:17.185431', 0, 'officer1', '', '', 'off1@test.org', 0, 1, '2022-07-25 10:56:40.902797');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(7, 'accounts', 'logininfo'),
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(8, 'home', 'items'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2022-07-25 05:08:07.279989'),
(2, 'auth', '0001_initial', '2022-07-25 05:08:07.746529'),
(3, 'admin', '0001_initial', '2022-07-25 05:08:07.883406'),
(4, 'admin', '0002_logentry_remove_auto_add', '2022-07-25 05:08:07.903243'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2022-07-25 05:08:07.915066'),
(6, 'contenttypes', '0002_remove_content_type_name', '2022-07-25 05:08:07.986291'),
(7, 'auth', '0002_alter_permission_name_max_length', '2022-07-25 05:08:08.040791'),
(8, 'auth', '0003_alter_user_email_max_length', '2022-07-25 05:08:08.057048'),
(9, 'auth', '0004_alter_user_username_opts', '2022-07-25 05:08:08.066561'),
(10, 'auth', '0005_alter_user_last_login_null', '2022-07-25 05:08:08.115642'),
(11, 'auth', '0006_require_contenttypes_0002', '2022-07-25 05:08:08.115642'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2022-07-25 05:08:08.132509'),
(13, 'auth', '0008_alter_user_username_max_length', '2022-07-25 05:08:08.156352'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2022-07-25 05:08:08.188030'),
(15, 'auth', '0010_alter_group_name_max_length', '2022-07-25 05:08:08.215385'),
(16, 'auth', '0011_update_proxy_permissions', '2022-07-25 05:08:08.229124'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2022-07-25 05:08:08.259582'),
(18, 'sessions', '0001_initial', '2022-07-25 05:08:08.307631'),
(19, 'accounts', '0001_initial', '2022-07-25 06:17:54.212145'),
(24, 'home', '0001_initial', '2022-07-26 10:57:07.359884'),
(25, 'home', '0002_auto_20220726_1650', '2022-07-26 11:20:42.217425'),
(26, 'home', '0003_auto_20220726_1654', '2022-07-26 11:25:03.397975'),
(27, 'home', '0004_auto_20220729_0140', '2022-07-28 20:11:06.109910');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('dm7ffa4jdnlmsneasqxrgqlx7cni0676', '.eJxVjDsOwjAQBe_iGlnxP6akzxmsXduLA8iW4qRC3J1ESgHtm5n3ZgG2tYSt5yXMiV2ZZZffDSE-cz1AekC9Nx5bXZcZ-aHwk3Y-tZRft9P9OyjQy15nENLgaBTRMHoyCkwWhDGSl16lwekowROhdlZTwqiVFFI7snanZNnnC_tqOEA:1oHAyN:2cDopfV3uO10En8BWJny15IzDc5pyhYlIX8OzoyZhNI', '2022-08-11 21:23:11.980409'),
('frv6oldwnf0i6swkzyc4dbx16pde649e', '.eJxVjDsOwjAQBe_iGlnxP6akzxmsXduLA8iW4qRC3J1ESgHtm5n3ZgG2tYSt5yXMiV2ZZZffDSE-cz1AekC9Nx5bXZcZ-aHwk3Y-tZRft9P9OyjQy15nENLgaBTRMHoyCkwWhDGSl16lwekowROhdlZTwqiVFFI7snanZNnnC_tqOEA:1oGR63:s3t_6pY0nbiqXuIegDxFeDHTsNEOgoqfX5eFTO9j7uk', '2022-08-09 20:24:03.035894'),
('fux3cgw7ko38ene145wwkeb5p7oznfu9', '.eJxVjDsOwjAQBe_iGlnxP6akzxmsXduLA8iW4qRC3J1ESgHtm5n3ZgG2tYSt5yXMiV2ZZZffDSE-cz1AekC9Nx5bXZcZ-aHwk3Y-tZRft9P9OyjQy15nENLgaBTRMHoyCkwWhDGSl16lwekowROhdlZTwqiVFFI7snanZNnnC_tqOEA:1oHIaj:d3LqqqMEd04NV4xav6JQVIpg4HX1H2hOzeOZu_L6Mzc', '2022-08-12 05:31:17.193372'),
('i0t7z1kgc2q6kbl5m80ci0knhega0e2y', '.eJxVjDsOwjAQBe_iGlnxP6akzxmsXduLA8iW4qRC3J1ESgHtm5n3ZgG2tYSt5yXMiV2ZZZffDSE-cz1AekC9Nx5bXZcZ-aHwk3Y-tZRft9P9OyjQy15nENLgaBTRMHoyCkwWhDGSl16lwekowROhdlZTwqiVFFI7snanZNnnC_tqOEA:1oH8MD:FKcu2wj7UD7qPrE9hY6uYdnXPkA4VnVmh_YyBLGvXmc', '2022-08-11 18:35:37.299117'),
('ijmzm3k87mcxb9fgijp7lonh9vzd9d4m', '.eJxVjDsOwjAQBe_iGlnxP6akzxmsXduLA8iW4qRC3J1ESgHtm5n3ZgG2tYSt5yXMiV2ZZZffDSE-cz1AekC9Nx5bXZcZ-aHwk3Y-tZRft9P9OyjQy15nENLgaBTRMHoyCkwWhDGSl16lwekowROhdlZTwqiVFFI7snanZNnnC_tqOEA:1oG4AF:5uUr6TIp5bvUPWHFnbQ6c77tJiLkuxJBleJAsvLA7D8', '2022-08-08 19:54:51.549138'),
('w1lcevwmlrauplosruze8jh2hghkh1x6', 'e30:1oFrOH:Kl4Hu2MmLvIXzsU05OVfsQ-QBXfT63OloxLYGNpjpyw', '2022-08-08 06:16:29.832958'),
('ycskpplzt7vw7vbld07lq247prx8gyow', '.eJxVjDsOwjAQBe_iGlnxP6akzxmsXduLA8iW4qRC3J1ESgHtm5n3ZgG2tYSt5yXMiV2ZZZffDSE-cz1AekC9Nx5bXZcZ-aHwk3Y-tZRft9P9OyjQy15nENLgaBTRMHoyCkwWhDGSl16lwekowROhdlZTwqiVFFI7snanZNnnC_tqOEA:1oFvlR:o9B1VkktVPbbGWl4dlN00_pccKkz6FjHZ9OUV46E5_s', '2022-08-08 10:56:41.358654');

-- --------------------------------------------------------

--
-- Table structure for table `home_items`
--

CREATE TABLE `home_items` (
  `id` bigint(20) NOT NULL,
  `Product_sr_no` varchar(30) NOT NULL,
  `item_name` varchar(200) NOT NULL,
  `year_of_purchase` date NOT NULL,
  `fund_name` varchar(200) NOT NULL,
  `LP_NO` varchar(5) NOT NULL,
  `initial_price` double NOT NULL,
  `issued_to` varchar(100) NOT NULL,
  `Depreciated_Price` double NOT NULL,
  `Remarks` longtext NOT NULL,
  `barcode` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `home_items`
--

INSERT INTO `home_items` (`id`, `Product_sr_no`, `item_name`, `year_of_purchase`, `fund_name`, `LP_NO`, `initial_price`, `issued_to`, `Depreciated_Price`, `Remarks`, `barcode`) VALUES
(33, 'dfwq', 'dwd', '2020-05-12', 'wh123', 'asdc', 1312, 'Mr.y', 23, 'test4', 'barcodes/30WH2020DW.png'),
(37, 'ab1234', 'qxxw', '2004-11-12', 'wdf', 'xqed', 213212, 'MR.X', 213, 'dup add entry post', 'barcodes/30WD2004QX.png'),
(40, 'ah213', 'azsedrf', '2020-11-12', 'qa231', 'qw213', 2341.21, 'MR.X', 12.21, 'import', 'barcodes/30QA2020AZ.png');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `accounts_logininfo`
--
ALTER TABLE `accounts_logininfo`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `home_items`
--
ALTER TABLE `home_items`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `home_items_Product_sr_no_4d00524f_uniq` (`Product_sr_no`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `accounts_logininfo`
--
ALTER TABLE `accounts_logininfo`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT for table `home_items`
--
ALTER TABLE `home_items`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `accounts_logininfo`
--
ALTER TABLE `accounts_logininfo`
  ADD CONSTRAINT `accounts_logininfo_user_id_2a0cfaf2_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
